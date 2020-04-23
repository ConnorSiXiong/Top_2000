def rangeBitwiseAnd(m: int, n: int) -> int:
    if len(bin(m)) != len(bin(n)):
        return 0
    move = 0
    while m != n:
        print('------')
        print('m ', m)
        print('bin(m)1 ', bin(m))

        print('n ', n)
        print('bin(n)1 ', bin(n))
        m >>= 1
        print('m ')
        print('bin(m)2 ', bin(m))
        n >>= 1
        print('n ')
        print('bin(n)2 ', bin(n))

        move += 1

    return m << move


m = 5
n = 7

rangeBitwiseAnd(m, n)


