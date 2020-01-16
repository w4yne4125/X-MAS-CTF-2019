a_ = '1011010100010011111001001100000010011101010111100001101100111001'
poly_ = '1010101000001101001110100110011101111110000110111110000010111111'
# out[0] = a[0]
# out[1] = a[1] ^ out[0]
# out[2] = a[2] ^ out[0] ^ out[1]
# out[3] = a[3] ^ out[0] ^ out[1] ^ out[2]
# ...
# out[6] = a[6] ^ out[0] ^ out[1] ^ ... ^ out[5] = a[6] ^ a[5]
# out[7] = a[7] ^ out[1] ^ out[2] ^ ... ^ out[5] ^ out[6] = a[7] ^ a[6] ^ a[0]
# out[8] = a[8] ^ out[0] ^ out[2] ^ ... ^ outp

# out[64] = a[64] ^ out[0] ^ out[2] ^ out[4] ^ ...
# out[65] = a[65] ^ out[1] ^ out[3] ^ out[5] ^ ...

def int2bits(x, nbits):
    x = bin(x)[2:].rjust(nbits, '0')
    assert len(x) == nbits
    return x

def xor(a, b, nbits):
    return int2bits(int(a, 2) ^ int(b, 2), nbits)

def select(o):
    ret = 0
    for i in range(64):
        ret ^= int(o[i]) * int(a_[i])
    return ret

out = []
is_one = []
for i in range(64):
    if poly_[i] == '1':
        is_one.append(i)
for i in range(4300):
    out.append('0' * 64)
    if i < 64:
        out[i] = out[i][:64 - i - 1] + '1' + out[i][64 - i:]
    for j in is_one:
        if i - 64 + j < 0:
            continue 
        out[i] = xor(out[i], out[i - 64 + j], 64)
A = []
for i in range(1, 101):
    A.append(list(map(int, list(out[43 * i - 1]))))
print(A)

a = matrix(GF(2), A)
exec(raw_input())
c = vector(GF(2), right)
print 'state = ',
print a \ c