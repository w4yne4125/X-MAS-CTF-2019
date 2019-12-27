import os

class PRNG(object):
	def __init__(self, length):
		self.length = length
		self.state = self.getseed()
		self.key = self.getseed()

	def parity(self,x):
		aux = self.length
		while aux > 1:
			x ^= x >> ((aux + 1) / 2)
			aux = (aux+1) / 2
			
		return x & 1
	
	def getseed(self):
		return int(os.urandom(self.length / 8).encode('hex'), 16)
	
	def next_state(self):
		self.state = (self.state >> 1) | (self.parity(self.state & self.key) << (self.length - 1))
		
	def get_bit(self):
		output = self.state & 1
		self.next_state()
		return output
		
	def get_bits(self, bits):
		output = 0
		for i in range(bits):
			output = (output << 1) + self.get_bit()
		return output