# FUNction Plotter

> Author: disam | 王松億 | B06705049

### Description

One of Santa's elves found this weird service on the internet. He doesn't like maths, so he asked you to check if there's anything hidden behind it.

Remote Server: nc challs.xmas.htsp.ro 13005 Author: yakuhito

source: [server](./server)

### Solution

他會要求我們回答961次某個function的答案，而可以觀察到答案不是0就是1，因此寫一個腳本跑一次就可以知道所以答案，並且用一個案維陣列存起來(text.txt)，而因為961是31x31，因此把這些答案用31x31列印出來可以看出是一張QR code。
最後用PIL library將1的pixal塗成黑色，0的pixal塗成白色，即可得到flag的QR code。
