class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = len(t)

        candidates = []
        shortest = float('inf')
        res = ''
        t_dict = self.generateTargetDict(t)
        print(t_dict)
        while left != right and right <= len(s):
            sub = s[left: right]
            print('sub', sub)
            if self.checkExist(sub, t_dict.copy()):
                candidates.append(sub)
                if len(sub) < shortest:
                    res = sub
                    shortest = len(sub)
                left += 1
            else:
                if right < len(s):
                    right += 1
                else:
                    left += 1
        print(candidates)
        print('res', res)
        return res

    def checkExist(self, comb, target_dict):
        print('comb', comb)
        for i in comb:
            if i in target_dict.keys():
                target_dict[i] -= 1

        for i in target_dict.keys():
            if target_dict[i] > 0:
                return False
        return True

    def generateTargetDict(self, target):
        target_dict = {}

        for i in target:
            if i in target_dict.keys():
                target_dict[i] += 1
            else:
                target_dict[i] = 1
        return target_dict

S = "ADOBECODEBANC"
T = "ABC"

# S = 'aa'
# T = 'aa'

a = Solution()
a.minWindow(S, T)
