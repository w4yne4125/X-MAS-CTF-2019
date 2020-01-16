from pwn import *
y = remote('eductf.zoolab.org', 20003)

prev = 1.1
c = []
for i in range(100):
    y.sendlineafter('> ', str(0))
    now = float(y.recvline())
    print(now)
    if now < prev:
        c.append(1)
    else:
        c.append(0)
    prev = now

print 'right = ',
print c
exec(raw_input()) # enter the state
state = int(''.join(map(str, state)), 2)
poly = 0xaa0d3a677e1be0bf
def step():
    global state
    out = state & 1
    state >>= 1
    if out:
        state ^= poly
    return out

def random():
    for _ in range(42):
        step()
    return step()
c2 = []
for i in range(100):
    c2.append(random())
print(c2)
while 1:
    try:
        y.sendlineafter('> ', str(random()))
        print(y.recvline())
    except:
        y.interactive()
        exit(0)