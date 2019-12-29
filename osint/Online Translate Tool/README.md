# Online Translate Tool

> Author: weibig | 陳惟中 | B06705014, devin6011 | 林首志 |

### Description


### Solution

一開始點進那個連結，footer 有製作人的名字，去搜他的 github 就找到此網站的原始碼，查看他 repo 紀錄看到一個 secret file，裡面有500多張看起來一樣的照片。
但後來發現有些圖片的檔案大小會多出2個bytes，這些圖片照檔案名稱排序後，把他們的倒數第二個byte接起來，就找到 flag 了！