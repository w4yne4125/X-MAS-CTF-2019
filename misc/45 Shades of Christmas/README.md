# Santa's letter

> Author : wayneOuO | 吳崇維 | B06902058

### Problem Description

Given a png file, try to get flag.

### Solution 

After converting the image to np array, it can be found that all the values' corresponding character under ASCII is printable, and are symbols used in base64 encoding.

By observing the distribution of the characters, we can derive the message by decoding the Transposed image's values.

