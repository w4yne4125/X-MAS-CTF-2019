# What's Up, Santa?

> Author: howard41436 | 楊皓丞 | B06902097

### Description

You really want to get that top of the line Pentium III processor this Christmas, but Santa doesn’t want to get it for you! You need to trick the old man into thinking that he has already promised you one by sending him a message replying to him saying “I will gift you the Pentium III processor this Christmas” (on Santa’s WhatsApp account it should appear as if he has told you this, even though he has never sent you such a message).

WhatsApp phone number: +xx xxx xxx xxx

### Vulnerability

WhatsApp vulnerability, disclosed on [Black Hat 2019](https://research.checkpoint.com/2019/black-hat-2019-whatsapp-protocol-decryption-for-chat-manipulation-and-more/?fbclid=IwAR3U7JKYsW-RxxyC18ivaZZDJVYjCRKzkZkET5q2Blt4wGdYRYUe_hX7Cb8).

### Solution

I mainly followed the method described in the above link, and also I found a [step-by-step guide](https://www.youtube.com/watch?v=do_4bEI3Ahs&fbclid=IwAR3rLpSPFM-lytAMQ00-d2mXwfuHT5d_QMKJIuNR_o6vvbmDijQdXJl3lfo) which is very helpful. The video teaches how to manipulate the message sent by a user to you, and reply the message, tricking that user into believing that he sent that message before, even though he didn't. Most of the video is correct, but take note of the following two points: 1. The ref object that needs to be pasted into BurpSuite should start from `"ref"` instead of `["Conn",` in the video; 2. In addition to manipulating the message of the user, we need to change(increase) the id of the incoming message too. I failed many time at first because of this reaseon, where I see the modified message on my side, but when I replied the message, the replied message on the user's screen is the original message he sent. This is because the original message is already stored in the database with that specific id, so we need to change the id of the manipulated message for the attack to work. Now I can implement the attack shown in the video.

However, this challenge is slightly harder because Santa won't send me any messages for me to manipulate. In the Black Hat 2019 website about this attack, there is an attack that can manipulate a message sent by me to a user, where I can change the `fromMe` field from `True` to `False`, then it will appear as a message send from the user. However, this doesn't work on my computer (I think it is patched already because I discovered that it doesn't work on other people's computer either after the contest ended). So I tried to manipulate a user's message to me, and instead of changing the message, I want to change the sender of the message, so my client thinks that it's Santa sending the message. To do this, we need to manipulate the `remoteJid` field in addition to `message` field, but it failed on my first few tries. Observing the incoming and outgoing packets in BurpSuite, I found out that some packets holds the `remoteJid` of the user I'm having a conversation with. After changing those field into Santa's `remoteJid` too, it worked and I received Santa's message saying “I will gift you the Pentium III processor this Christmas”. After replying to this message, Santa sent me the flag.