def bitwiseComplement(N: int) -> int:
    binary_str = "{0:b}".format(N)
    res_str = ''
    for i in binary_str:
        if i == '0':
            res_str += '1'
        else:
            res_str += '0'

    return int(res_str, 2)
