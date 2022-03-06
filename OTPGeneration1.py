"""
Generating OTP using Random library
"""
import random

def generate():
	rn = random.randrange(10**(1023-1), 10**1023)
	num = list(str(rn))
	pos = list(range(1023))
	random.shuffle(pos)
	otp = []
	for i in range(6):
		x = pos.pop()
		print(num[x])
		otp.append(num[x])
	otp = ''.join(otp)
	print('1023 digit random number: ', rn)
	print('6 digit OTP: ', otp)

generate()