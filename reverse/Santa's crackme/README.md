# Santa's crackme

> Author: disam | 王松億 | B06705049

### Description

I bet you can't crack this!

source: [main](./main)

### Solution

Firstly, I reversed the binary with IDA PRO. And I found that the program just do
```{c++}
for (int i = 0; license[i] != '\0'; i++) {
    tmp[0] = license[i] ^ 0x3;
    tmp[1] = '\0';

    ok |= strcmp(tmp, flag_matrix[i]);
}
```
Thus, I found the flag after doing the XOR again.