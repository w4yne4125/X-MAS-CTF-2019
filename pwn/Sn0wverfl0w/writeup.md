# Sn0wverfl0w

> Author : wayneOuO | 吳崇維 | B06902058

### Problem Description

The binary will simply `gets` a string, with no canary protection. Also the binary has a function that print flag.

### Solution 

**Stack Overflow**. By modifying the return address of main, we can jump to the print flag function.

