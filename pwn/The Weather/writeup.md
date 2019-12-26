# The Weather

> Author : wayneOuO | 吳崇維 | B06902058

### Problem Description

Connect to the server, then the server will respond a binary with base64 encoded. This binary will simply `gets` a string, with PIE and canary disabled.

### Solution 

With the binary get from server, we can use technique like **ROPgadget on ret2csu** to leak libc address then jump to `system`.

The problem is that, in fact, the binary that sent from server is not the same. So the information such as the address of `got table` or the address `csu_init` is changing from time to time.

So we can come up with a solution : Connect to the server  (with timeout) $\Rightarrow$ Analyze the binary  $\Rightarrow$ Send payload to the server within the same connection.

 



