from pwn import *
rem = [remote('eductf.zoolab.org', 20002), remote('eductf.zoolab.org', 20002)]
# rem = [remote('140.112.31.102', 8888), remote('140.112.31.102', 8888)]
ns = []
es = []
tickets = []
for r in rem:
    r.sendlineafter('> ', str(1))
    ns.append(int(r.recvline().strip().split('= ')[1]))
    es.append(int(r.recvline().strip().split('= ')[1]))
    tickets.append(r.recvline().strip().split('= ')[1])

print(ns)
print(es)
print(tickets)
assert len(tickets[0]) == len(tickets[1]) == 1280
# FLAG = '}DLoSteGREVENC'
FLAG = ''
pipe = 124
for j in range(len(FLAG), 16):
    guess = [[], []]
    for i in range(2):
        for c in range(32, 126 + 1):
            if c == pipe:
                continue
            delta = c - pipe
            t = tickets[i]
            new = t[:-512] + hex((int(t[-512: -256], 16) + (256 ** j) * delta) % ns[i])[2:] + t[-256:]
            rem[i].sendlineafter('> ', str(2))
            rem[i].sendlineafter('= ', str(new[:-256]))
            reply = rem[i].recvline()
            rep1 = 1 if 'Pass' in reply else 0
            print(reply, rep1)
            rem[i].sendlineafter('> ', str(2))
            rem[i].sendlineafter('= ', str(new))
            reply = rem[i].recvline()
            rep2 = 1 if 'Pass' in reply else 0
            # print(reply, rep2)
            # print('-' * 20)
            if rep1 != rep2:
                guess[i].append(c)
    ch = list(set(guess[0]) | set(guess[1]))
    print(ch)


exit(0)