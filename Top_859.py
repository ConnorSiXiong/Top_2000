def buddyStrings(A: str, B: str) -> bool:
    if len(A) != len(B):
        return False

    if len(A) == 0 or len(B) == 0 or len(A) == 1 or len(B) == 1:
        return False

    A = list(A)
    B = list(B)

    if A == B:
        twice_check = set()

        for i in A:
            twice_check.add(i)
        if len(twice_check) == len(A):
            return False
        return True

    anchor_one = -1
    anchor_two = -1

    for i in range(len(A)):
        char_a = A[i]
        char_b = B[i]
        if char_a != char_b:
            if anchor_one == -1:
                anchor_one = i
            else:
                anchor_two = i
                break

    if anchor_two == -1:
        return False

    temp = A[anchor_one]
    A[anchor_one] = A[anchor_two]
    A[anchor_two] = temp
    if A == B:
        return True
    else:
        return False


a = 'abb'
b = 'abb'

print(buddyStrings(a,b))