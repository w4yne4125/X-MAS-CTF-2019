# Ponzi Scheme

> Author : disam | 王松億 | B06705049

### Problem Description

Just trust me and you'll make a fortune. For PoW, you can use these provided scripts. Note: This is NOT a web challenge. There is no intended vulnerability in the web application.
http://eductf.zoolab.org:17385
author: bookgin


### Solution 
一開始想說只要寫個腳本讓他一直投資最小報酬率的plan就好，但後來才發現Ponzi不一定一直都有足夠的錢給我們，如果Ponzi沒錢就會導致我們破產。後來楊皓丞想到創好大量帳號並一次投資讓Ponzi有足夠金錢的辦法。
因此，為了能夠讓Ponzi在某個瞬間有足夠的10000，我們總共創了11個人，並用其中一個人投資報酬率最大的那個plan並開始計時，等到計時器快到1 hour的時候（3598秒）再讓其他10個人都投資任何一個plan，這樣Ponzi就會有足夠的錢給我們了。
