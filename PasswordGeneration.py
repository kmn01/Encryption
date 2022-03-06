"""
Generating hard to crack but easy to remember password from given text

A password can be considered strong if it is a combination of upper and lower case characters, numbers, symbols.
To ensure that the password is also easy to remember, this algorithm substitutes randomly chosen 20% of the alphabets in the input string with intuitive alternative numbers or symbols as defined in the key and changes the case of 10% of the alphabets in the input string. 
Longer password are stronger but with increased length, the memorability also decreases. Hence, this program enforces a minimum length of 8 for the input string that would be converted to a strong password of the same length.
"""
import random
import math
key = ['@', '8', '(', ')', '^', '7', '9', '#', '!', ']', '<', '1', '3', '4', '0', '?', '&', '%', '5', '[', '6', '>', '}', '/', '$', '2']

def crypt(s):
	n = len(s)
	pos = list(range(n))
	random.shuffle(pos)
	ctrsub1 = math.ceil(0.2*n)
	ctrsub2 = math.ceil(0.1*n)
	text = list(s)
	for i in range(ctrsub1):
		x = pos.pop()
		if text[x].isupper():
			text[x] = key[ord(text[x])-65]
		elif text[x].islower():
			text[x] = key[ord(text[x])-97]
	for i in range(ctrsub2):
		x = pos.pop()
		if text[x].isupper():
			text[x] = text[x].lower()
		elif text[x].islower():
			text[x] = text[x].upper()

	pswd = ''.join(text)
	return pswd

print('Enter string\nConstraints:\n* Plain english\n* No spaces\n* Max length 100\n* Min length 8')
s = input()
if len(s) >= 8:
	print('Password: ', crypt(s))
else:
	# to ensure strong password, minimum string length is 8
	print('String is too short to form a strong password')	