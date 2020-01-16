# RSACTR

> Author: howard41436 | 楊皓丞 | B06902097

### Solution

本題中，可以給一次任意的明文來得到加密完的密文，且可以得到一次加密完的flag。若我們一開始輸入明文`'a' * 16`，會得到密文`cipher == (nonce ** d + int("a" * 16, 16)) % n`，那麼我們可以知道`(cipher - int("a" * 16, 16)) ** 3 % n == nonce`，也就是我們可以知道`nonce`的值。接下來，對於加密完的flag的第一部份`flag1`，我們可以知道他加密完的值會是`val == ((nonce + 2020) ** d + flag1) % n` ，令方程式`f(x) = (val - x) ** 3 % n`，則`f(flag1) == nonce + 2020`，也就是代表`flag1`為`f(x) - nonce - 2020`的根。再來發現說`n`和`nonce`都是128 bytes，但是`flag1`是16 bytes，也就是`flag1`是此方程式的小根，可以用coppersmith method來解。其餘兩部分的flag同理。使用的程式碼`sol.sage.py`放在`code/`資料夾中。