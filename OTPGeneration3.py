"""
Generating 100 OTPs
"""
import random
import time

def generate_100otp():
	rn = random.randrange(10**(1023-1), 10**1023)
	print('1023 digit random number: ', rn)
	num = list(str(rn))
	pos = list(range(1023))
	random.shuffle(pos)
	ctr = 0
	otps = []
	while ctr < 100:
		otp = []
		for i in range(6):
			x = pos.pop()
			otp.append(num[x])
		otp = ''.join(otp)		
		if otps.count(otp) == 0:	# ensures uniqueness
			print(ctr+1, otp)
			otps.append(otp)
			ctr += 1

start_time = time.time()
generate_100otp()
print("\nExecution time in seconds: ", (time.time() - start_time))