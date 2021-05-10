def strStr(source, target):
    # Write your code here
    if len(target) > len(source):
        return -1
    """
    这里有一个知识盲点
    target = ""
    是任意其他string的子集
    
    https://stackoverflow.com/questions/18399189/why-does-contains-method-find-empty-string-in-non-empty-string-in-java
    """
    if len(target) == 0:
        return 0

    for i in range(len(source)):
        for j in range(len(target)):
            if source[i] == target[j]:
                if len(target) <= len(source) - i:
                # 这个地方一开始写成了 len(target) >= len(source) - i
                # 写反了
                    if source[i: i+len(target)] == target:
                        return i
                    else:
                        continue
                else:
                    return -1
    return -1
a = ''
b = ''
print(strStr(a, b))


