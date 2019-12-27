# Mercenary Hat Factory

> Author: howard41436 | 楊皓丞 | B06902097

### Description

"Mmph Mmmmph Mmph Mmmph!"
Translation: Come and visit our hat factory!

source: [server.py](server.py)

### Vulnerability

JWT, Python Features, SSTI

### Solution

This is a very interesting web challenge and I applied many knowledge learned in class.

The keypoint is before we can "make hats", which seems to be the website's main usage, we need to be an authorized admin. This takes two steps, we need to first become an admin, then we need to authorized ourself to proof that we are the Santa Claus.

The website used JWT, which is used as signed cookies to carry user data and prevent us from modifying the content. Basically, we want to change `{'type': 'user', 'user': 'howard'}` to `{'type': 'admin', 'user': 'howard'}`. Let us first observe what a JWT token looks like. A JWT token `a.b.c`, consists of `a`: the JWT header where the signing algorithm is specified, `b`: the JSON data it carries, and `c`: the signature of `a.b`. All three parts are base64 encoded. If used correctly, we cannot calculate the signature part without knowing the secret key if we want to modify the data part. However, since the JWT header carries its signing algorithm, if the server decodes the JWT token according to the algorithm specified in the header instead of the algorithm it used to encode it originally, there will be a vulnerability. JWT tokens support a signing algorithm `None`, meaning that the no signature will be used. Therefore, we can craft a JWT token, `base64("{"alg":None},{"typ":JWT}").base64("{"type":"admin","user":"howard"}").`, and this will pass the JWT decode check if it is not implemented correctly. This method succeeded in this challenge, and we logged in as an admin.

Now, we need to authorize ourself. `adminPrivileges[uid]` is a 3-element list, `[uid, username, privilegeCode]`, where `username` is our username, `uid` is calculated using the hash of our username, and `privilegeCode` is a value we can enter in the first step of authorization. In the second step of verification, we need to enter a string that equals to `str(uid) + Santa's username + Santa's privilegeCode + privilegeCode `, where Santa's username is "Santa" but we don't know SantaSecret, Santa's privilege code. But is it? The list of lists `adminPrivileges` is declared using `adminPrivileges = [[None]*3]*500`, and we know that in python, lists are passed as reference, so actually all 500 entries of the list share the same list reference, and when we modify one entry, the others are modified too. Therefore, after we finish the first step authorization, Santa's username has already become our username, and Santa's privilege code has already become ours too. Therefore, assume in first step authorization I entered "haha" as the privilege code, in the second step, the access code is `str(uid) + "howard" + "haha" + "haha"`, and we successfully become a authorized admin.

Now, we can make hats. The process of making hat is we enter the hat's name, then the website will show a random hat image and the name we entered. When I entered `7*7` the name showed on screen is `49`, so it is vulnerable to SSTI. After some tries it appears to be Jinja, and by the source code we know that the server runs in python3. The server blacklisted `["config", "self", "request", "[", "]", '"', "_", "+", " ", "join", "%", "%25"]`, and limited the use of `","` to once. Observe that `'` isn't blacklisted, and we can bypass any blacklist in strings using hex encoding. In Jinja, there is a pipeline operator `| `;`a|b` is equivalent to `b(a)`, and `a|b(c)` is equivalent to `b(a, c)`. So we can use this to avoid the use of commas. Also, in Jinja, `attr(a, 'b')` is equivalent to `a.b`, and in python, `a.__getitem__(b)` is equivalent to `a[b]`. These are enough for us to bypass the blacklist. First, `session` is a global variable that always exsists, so we can use `session|attr('\x5f\x5fclass\x5f\x5f')` to find its class, then use `__base__` iteratively until we find `<class 'object'>`. The payload `session|attr('\x5f\x5fclass\x5f\x5f')|attr('\x5f\x5fbase\x5f\x5f')|attr('\x5f\x5fbase\x5f\x5f')|attr('\x5f\x5fbase\x5f\x5f')|attr('\x5f\x5fbase\x5f\x5f')` results in ``<class 'object'>``. Then we can use `__subclasses__()` method and see the list on the screen, find the index of `os._wrap_close`, which is 127 in my case. Then, we can use `.__init__.__globals__`, and we will see a dictionary. Now, we access the function `popen`, and we can RCE. When we execute `ls`, we find out that there is a `unusual_flag.mp4`, so we can't directly see the flag, it is probably in the video. So we execute `base64 unusual_flag.mp4`, and copy the result to local then decode it into a mp4 file. At last, open the video and the flag is inside.

Full payload: 

```jinja2
http://challs.xmas.htsp.ro:11005/makehat?hatName={{session|attr('\x5f\x5fclass\x5f\x5f')|attr('\x5f\x5fbase\x5f\x5f')|attr('\x5f\x5fbase\x5f\x5f')|attr('\x5f\x5fbase\x5f\x5f')|attr('\x5f\x5fbase\x5f\x5f')|attr('\x5f\x5fsubclasses\x5f\x5f')()|attr('\x5f\x5fgetitem\x5f\x5f')(127)|attr('\x5f\x5finit\x5f\x5f')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('popen')('base64\x20unusual\x5fflag.mp4')|attr('read')()}}
```