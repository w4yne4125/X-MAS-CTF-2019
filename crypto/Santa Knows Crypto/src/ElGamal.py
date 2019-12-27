from Crypto.Util.number import *
from PRNG import PRNG

class ElGamal(object):
	def __init__(self, length, prime = None):
		self.prng = PRNG(256)
		self.length = length
		self.g = 2
		self.q = prime
		while self.q == None:
				p = self.next_prime(2**(length) + self.prng.get_bits(length))
				if ((2 * p + 1) % 8 == 3 or (2 * p + 1) % 8 == 5) and isPrime(2 * p + 1):
					self.q = 2 * p + 1

		self.x = self.prng.get_bits(self.length)
		self.h = pow(self.g, self.x, self.q)
		
	def next_prime(self, x):
		if x & 1 == 0:
			x += 1
		while not isPrime(x):
			x += 2
		return x
		
	def encrypt(self, message):
		y = self.prng.get_bits(self.length)
		s = pow(self.h, y, self.q)
		c1 = pow(self.g, y, self.q)
		c2 = message * s % self.q
		return y, c1, c2
