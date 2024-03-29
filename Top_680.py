def validPalindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return subValidPalindrome(s, left + 1, right) or subValidPalindrome(s, left, right - 1)
    return True


def subValidPalindrome(s, left, right):
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True
