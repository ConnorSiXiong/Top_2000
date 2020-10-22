from typing import List


def asteroidCollision(asteroids: List[int]) -> List[int]:
    res = []
    a = asteroids

    while a:
        cur = a.pop(0)
        if not res:
            res.append(cur)
        else:
            pre = res.pop()

            # 判断符号是否一样
            if pre * cur > 0:
                res.append(pre)
                res.append(cur)
            else:
                # 符号不一样
                while True:
                    if pre < 0:
                        res.append(pre)
                        res.append(cur)
                        break
                    elif pre > 0:
                        if abs(cur) == pre:
                            break
                        elif abs(cur) < pre:
                            res.append(pre)
                            break
                        else:
                            if res:
                                pre = res.pop()
                            else:
                                res.append(cur)
                                break
    return res


a = [-10, -2, 5]

print(asteroidCollision(a))
