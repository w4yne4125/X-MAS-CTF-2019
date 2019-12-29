from pwn import *
r = remote("challs.xmas.htsp.ro", 13005)

a = [["0"]*31 for i in range(31)]

r.recvuntil("Can you guess all 961 values?\n\n\n")

for i in range(961):
	s = r.recvuntil("=")
	s = s.decode("utf-8")
	num1 = s[s.find("(")+1:s.find(",")]
	num2 = s[s.find(",")+2:s.find(")")]
	idx1 = int(num1)
	idx2 = int(num2)
	r.sendline(a[idx1][idx2])

	result = r.recvuntil("!")
	if result.decode("utf-8") != "Good!":
		a[idx1][idx2] = "1"
		print("f(%s, %s)=%s"%(num1,num2,a[idx1][idx2]))
	else:
		print("f(%s, %s)=%s"%(num1,num2,a[idx1][idx2]))

r.close()

f = open("text.txt", "w")
for i in range(31):
	for j in range(31):
		f.write("%s\n"%(a[i][j]))

r = remote("challs.xmas.htsp.ro", 13005)

r.recvuntil("Can you guess all 961 values?\n\n\n")
for i in range(961):
	s = r.recvuntil("=")
	s = s.decode("utf-8")
	num1 = s[s.find("(")+1:s.find(",")]
	num2 = s[s.find(",")+2:s.find(")")]
	idx1 = int(num1)
	idx2 = int(num2)
	r.sendline(a[idx1][idx2])

	result = r.recvuntil("!")
	if result.decode("utf-8") != "Good!":
		print("f(%s, %s) is wrong!"%(num1,num2))
	else:
		print("f(%s, %s) is correct!"%(num1,num2))
r.interactive()