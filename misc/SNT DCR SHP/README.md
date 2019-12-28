# SNT DCR SHP

> Author: howard41436 | 楊皓丞 | B06902097

### Description

Santa has opened a new decoration shop in place of the corner store. Will it be able to dominate the market or will it fail victim to hackers?

source: [server.py](./server.py)

### Vulnerability

Python Format String

### Solution

In the class method `print_decoration`, it prints the format string `('{0.quantity} x ... '+ self.type).format(self)`, where `self.type` is fully controlled by us. We can use format string in `self.type` too. Therefore, set `self.type = "{0.__init__.__globals__}"`, then it will print out all the global symbols, including the flag imported from a secret file.