import gmpy2 as gp
"""
RSA ALGORITHM IMPLEMENTATION
The steps in an RSA Algorithm are
1. Choose two prime numbers p, q.
2. Let n = p * q
3. Let φ = (p − 1)(q − 1)
4. Choose a large number e ∈ [2, φ − 1]that is coprime to φ.
5. Compute d ∈ [2, φ − 1] such that e × d = 1 (mod φ), and d must be coprime to φ
6. (e, n) is the public key
7. (d, n) is the private key
8. Encryption: C = m^e(mod n)
9. Decryption: m = C^d(mod n)
"""

def encrypt(p, q, m):
	n = gp.mul(p, q)
	phi = gp.mul(gp.sub(p, 1), gp.sub(q, 1))
	if 65537 < phi and gp.gcd(65537, phi) == 1:
		e = 65537
	elif 257 < phi and gp.gcd(257, phi) == 1:
		e = 257
	elif 17 < phi and gp.gcd(17, phi) == 1:
		e = 17
	elif 5 < phi and gp.gcd(5, phi) == 1:
		e = 5
	elif 3 < phi and gp.gcd(3, phi) == 1:
		e = 3
	else:
		e = gp.sub(phi, 1)
	d = gp.divm(1, e, phi) # returns d such that e * d = 1 mod phi; since 1 mod phi, d is coprime to n
	c = gp.powmod(m, e, n)
	print('c: ', c)
	print('e: ', e)	
	print('d: ', d)
	print('n: ', n)
	return c, d, n

def decrypt(c, d, n):
	m = gp.powmod(c, d, n)
	print('m: ', m)

print('Enter p, q, m\nConstraints:\n* p<q\n* m<p*q\n* p and q are prime\n* p, q and m are integers of max 1023 digits:\n')
p = int(input('p: '))
q = int(input('q: '))
m = int(input('m: '))

print('\nRSA Encryption')
c, d, n = encrypt(p, q, m)

print('\nRSA Decryption')
decrypt(c, d, n)