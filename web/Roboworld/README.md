# Roboworld

> Author: howard41436 | 楊皓丞 | B06902097

### Description

A friend of mine told me about this website where I can find secret cool stuff. He even managed to leak a part of the source code for me, but when I try to login it always fails :(

Can you figure out what's wrong and access the secret files?

source: [leak.py](./leak.py)

### Vulnerability

HTTP Parameter Pollution, CAPTCHA Debugging Key

### Solution

In this problem, we have to login the website. Although the username and password is already given in the source code, the CAPTCHA value generator of the website is broken, and it now only generates random strings, making us unable to pass the CAPTCHA verification. 

The source code uses format string to format HTTP parameters, so we can pollute the parameters because when there are two or more parameters with same name, only the first one is effective. Therefore, we can control the `privateKey` parameter. In the source code, it gives us the private key used for debugging in the comment. Debugging private key for CAPTCHA will accept all CAPTCHA user values, so we can successfully login using the payload: `user=backd00r&pass=catsrcool&captcha_verification_value=haha%26privateKey%3d8EE86735658A9CE426EAF4E26BB0450E`. The flag is inside one of the videos provided after we logged in.