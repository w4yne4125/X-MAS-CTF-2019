# PokemonGo

> Author : wayneOuO | 吳崇維 | B06902058

### Problem Description

給定一個程式的log，接著要reverse他的進程。

### Solution 

觀察log會發現他其中有很多可以忽略的片段，例如初始(init)，Std I/O (scanf, printf)，都清掉之後就剩下簡單的程式邏輯，這個邏輯首先吃一個字串，接著將字串的值以如下的方式記錄下來：

a[0] + a[1] , a[1] + a[2], a[2] + a[3] , …. 

接著將這些值一個一個檢查，若是value都一樣就通過檢查。

因此reverse就很簡單了，把他一個一個檢查的value拿出來，並且假定a[0]的value ，就可以推出剩下的字元，從中選出最像的字串即可。

