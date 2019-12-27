# Rigged Election

> Author: howard41436 | 楊皓丞 | B06902097

### Description

Come one, come all! We've opened up a brand new website that allows the Lapland people to vote the next big town hall project! Just upload your ideas on the platform and vote using your CPU power. We've made sure voting takes a great amount of effort, so there's no easy way to play the system.

If you are indeed able to vote more than 250 times, you will be congratulated as an active Lapland citizen and receive a prize worthy of this title.

### Vulnerability

POW with fixed prefix and checks not long enough bits.

### Solution

The POW in the website is designed that if we vote using the browser interface, the POW takes tens of seconds each time, and to vote 250 times is very time-consuming. However, the expected tries to find one preimage is 16,777,216, which is less than a second if we use C/C++ language. Also, since the prefix is fixed, we can precompute and cache the results locally, then we can answer queries instantly everytime. In addition, I discovered that if we answer the POW incorrectly, the server will simply change a challenge string without any punishments, so we can just precompute about the first 10,000,000 to 20,000,000 strings and their hashes, instead of finding preimages for every possible hash. And if we encounter a hash not cached locally, we just randomly answer the server and the server will change a challenge string for us. My codes used for precompute the hashes and sending the requests are in the folder [code](code). The script takes only minutes to finish 250 votes, and after we vote 250 times, the flag will appear on the screen.