"""
Generating OTP using GMP library with time as seed
"""
import gmpy2 as gp
from datetime import datetime as dt

def generate():
	time = int(dt.now().timestamp()*1000)
	rn = 10**(1023-1) + gp.mpz_random(gp.random_state(time), 10**1023 - 10**(1023-1))
	num = list(str(rn))
	otp = []
	for i in range(6):
		x = gp.mpz_random(gp.random_state(), len(num))
		print(num[x])
		otp.append(num.pop(x))
	otp = ''.join(otp)
	print('1023 digit random number: ', rn)
	print('6 digit OTP: ', otp)

generate()