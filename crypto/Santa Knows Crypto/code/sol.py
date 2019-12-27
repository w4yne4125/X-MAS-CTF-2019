from pwn import *
from bma import *

rem = remote('challs.xmas.htsp.ro', 10000)
print(rem.recvline())
p = raw_input()
rem.send(p)

print(rem.recvuntil('q : '))
q = int(rem.recvline())
print('q = {}'.format(q))

print(rem.recvuntil('g : '))
g = int(rem.recvline())
print('g = {}'.format(g))

print(rem.recvuntil('c1 : '))
c1 = int(rem.recvline())
print('c1 = {}'.format(c1))

print(rem.recvuntil('c2 : '))
c2 = int(rem.recvline())
print('c2 = {}'.format(c2))

rem.sendlineafter('integer: ', '0')

print(rem.recvuntil('m : '))
m = int(rem.recvline())
print('m = {}'.format(m))

print(rem.recvuntil('y : '))
y = int(rem.recvline())
print('y = {}'.format(y))

def expand(a):
    t = bin(a)[2:]
    return '0' * (1024 - len(t)) + t
seq = [int(c) for c in expand(y)]
print('y_s = ', seq)
poly, span = Berlekamp_Massey_algorithm(seq)
poly = poly[-1:0:-1]
print(poly, span)

x = get_pre_n(poly, seq)
print('x = ', x)
x = ''.join([str(c) for c in x])
x = int(x, 2)

h = pow(g, x, q)

while 1:
    try:
        y = get_next_n(poly, seq)
        seq = list(y)
        y = ''.join([str(c) for c in y])
        y = int(y, 2)
        print(rem.recvuntil('c1 : '))
        c1 = int(rem.recvline())
        print('c1 = {}'.format(c1))

        print(rem.recvuntil('c2 : '))
        c2 = int(rem.recvline())
        print('c2 = {}'.format(c2))

        m = c2 * pow(pow(h, y, q), q - 2, q) % q
        rem.sendlineafter('integer: ', str(m)) 
    except:
        rem.interactive()
        exit()


