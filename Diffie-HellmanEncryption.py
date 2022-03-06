"""
Diffie-Hellman Implementation
"""

import gmpy2 as gp
from datetime import datetime as dt

def bob_sends_alice(p, g):
	time = int(dt.now().timestamp()*1000)
	b = 10**(1000-1) + gp.mpz_random(gp.random_state(time), 10**1000 - 10**(1000-1))
	B = gp.powmod(g, b, p)	# B = g^b (mod p)
	print('\nB: ', B)
	print('b: ', b)
	return B, b

def alice_sends_bob(p, g):
	time = int(dt.now().timestamp()*1000)
	a = 10**(1000-1) + gp.mpz_random(gp.random_state(time), 10**1000 - 10**(1000-1))
	A = gp.powmod(g, a, p)	# A = g^a (mod p)
	print('\nA: ', A)
	print('a: ', a)
	return A, a

def print_shared_secret_alice(B, a, p):
	s = gp.powmod(B, a, p)	# B^a(mod p)
	print('\nShared secret at Alice: ', s)

def print_shared_secret_bob(A, b, p):
	s = gp.powmod(A, b, p)	# A^b(mod p)
	print('\nShared secret at Bob: ', s)

print('Enter p, g\nConstraints:\n* p is prime\n* p and g are large integers\n* max 1023 digits\n')
p = int(input('p: '))
g = int(input('g: '))
B, b  = bob_sends_alice(p, g)
A, a = alice_sends_bob(p, g)
print_shared_secret_alice(B, a, p)
print_shared_secret_bob(A, b, p)