# winner winner chicken dinner

> Author: howard41436 | 楊皓丞 | B06902097

### Description

Winner, winner, chicken dinner! There it is. Thank you. God, I love this town. I love this game. And, Jim, I might even love you.

### Solution

這題的關鍵就是要解出這個PRNG的state，這樣我們就可以預測後面所有輸出，慢慢賺錢到贏得遊戲。分析之後可以發現`step[i]`(第`i`次呼叫`step()`的return value)是一個`Z(2)`底下，`state`的64個bit的線性函數。原因如下：`step[i]`的值即為原本`state`的第`ith significant bit`(若`i>=64`則為0)，加上每次這個bit對應到的`poly`中的bit是1時，那次的`step()`的return value，遞迴得知若之前的`step()`的return value都是`state`的64個bit的線性函數，那這次的也會是。由於`step[0] = state 的 LSB`，得證。

因此我們知道，我們最少需要看到64個step的return value，才能解出state(因為可能有一些式子是多餘的)，而我實測後發現一開始都用猜的話，大概有一半的機率在死前看到100個return value，足以解出`state`。把100條線性方程拿去用sage解之後就得到state了，得到後我們就能完美還原PRNG每次的輸出值，成功贏得遊戲。我使用`sol.sage.py`來產生方程式係數並且解方程式，並使用`send.py`跟server互動，此兩程式必須同時執行且互相手動輸入看到的值。程式碼都放在`code/`資料夾中。