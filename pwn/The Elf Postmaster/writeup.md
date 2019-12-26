# The Elf Postmaster

> Author : wayneOuO | 吳崇維 | B06902058

### Problem Description

Given a 64bit ELF file.

In this binary, there is a format string exploitation in a infinite loop, stops with a "end of letter" string. 

Things such as : 

```
while (string != "end of letter"):
	fgets(string)
	printf(string)
```

So we have infinite arbitrary read/write.

There are some limitations such seccomp, with open, read, write in the whitelist.

### Solution (Unsolved)

During the contest, I've leak many information such as libc address, main return address, PIE base…, etc. 

With arbitrary write, I try to control RIP, RSP to reach stack pivoting, by modifying return address to some gadgets.

Technically speaking, I should be able to modify return address and jump to gadget's chain to trigger open/read/write. The python script will work locally, but not for remote server.

 