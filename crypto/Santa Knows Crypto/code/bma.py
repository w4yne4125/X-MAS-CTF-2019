def Berlekamp_Massey_algorithm(sequence):
    N = len(sequence)
    s = sequence[:]

    for k in range(N):
        if s[k] == 1:
            break
    f = set([k + 1, 0])  # use a set to denote polynomial
    l = k + 1

    g = set([0])
    a = k
    b = 0

    for n in range(k + 1, N):
        d = 0
        for ele in f:
            d ^= s[ele + n - l]

        if d == 0:
            b += 1
        else:
            if 2 * l > n:
                f ^= set([a - b + ele for ele in g])
                b += 1
            else:
                temp = f.copy()
                f = set([b - a + ele for ele in f]) ^ g
                l = n + 1 - l
                g = temp
                a = b
                b = n - l + 1

    # output the polynomial
    def print_poly(polynomial):
        result = ''
        lis = sorted(polynomial, reverse=True)
        return lis
        for i in lis:
            if i == 0:
                result += '1'
            else:
                result += 'x^%s' % str(i)

            if i != lis[-1]:
                result += ' + '

        return result

    return (print_poly(f), l)

def get_pre(poly, observe):
    pos = -1 - min(poly) + 256
    ret = observe[pos]
    for i in poly[1:]:
        ret ^= observe[-1 - min(poly) + i]
    return ret

def get_pre_n(poly, obs, n = 1024):
    observe = obs[:256]
    ret = []
    for i in range(n):
        p = get_pre(poly, list(observe))
        ret = [p] + ret
        observe = [p] + observe[:-1]
    return ret

def get_next(poly, observe):
    ret = 0
    for i in poly:
        ret ^= observe[i]
    return ret

def get_next_n(poly, obs, n = 1024):
    observe = obs[-256:]
    ret = []
    for i in range(n):
        p = get_next(poly, list(observe))
        ret = ret + [p]
        observe = observe[1:] + [p]
    return ret