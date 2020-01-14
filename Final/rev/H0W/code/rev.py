from __future__ import print_function
import sys
from pwn import *
import string


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def one(x):
	return x ^ 0xfaceb00c

def rev_one(x):
	return x ^ 0xfaceb00c

def two(x):
	return x + 0x12384 

def rev_two(x):
	return x - 0x12384 

def thr(x):
	a = x & 0x5555555555
	b = x & 0xaaaaaaaaaa
	a = (a // 16) + (a % 16) * 2 ** 28
	b = (b % (2 ** 30)) * 4 + ( (b - (b % (2 ** 30))) // (2**30) )
	return a|b

def rev_thr(x):
	a = []
	for i in range(32):
		if (i % 2 == 0):
			a.append( (4 + i) % 32 )
		else:
			a.append( (31 + i - 1) % 32)
	res = 0
	for i in range(32):
		idx = 2 ** i
		if (x & idx):
			res = res | (2 ** a[i])
	return res


def four(x):
	return thr(two(one(x)))

def rev_four(x):
	return rev_one(rev_two(rev_thr(x)))

f3 = open("out", 'wb')

def convert(x):
	for i in range(4):
		y = x % 256
		f3.write(bytes([y]))
		x //= 256
	

f = open("refine", 'rb')
line = f.read()
f2 = open("seq", 'r')

for i in range(0, len(line), 4):
	ret = line[i : i+4]
	op = int(f2.readline())
	if (op == 0):
		convert(rev_one(u32(ret)))
	if (op == 1):
		convert(rev_two(u32(ret)))
	if (op == 2):
		convert(rev_thr(u32(ret)))
	if (op == 3):
		convert(rev_four(u32(ret)))
	if (i % 10000 == 0):
		eprint( i / len(line))



