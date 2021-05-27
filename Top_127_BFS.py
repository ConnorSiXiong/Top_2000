import pprint
from collections import defaultdict, deque
from time import sleep


def ladderLength(beginWord: str, endWord: str, wordList) -> int:
    # 去重
    wordList = set(wordList)

    if endWord not in wordList:
        return 0

    wordList.add(beginWord)

    # 每个单词的长度都是一样的
    l = len(beginWord)

    dic = defaultdict(list)
    # 这个字典就是
    # key - val
    # 抠出来一个char的单词 - 这个被抠出来的字符串，填上这个被抠出来的位置的char可能生成的在word list里的所有单词
    for word in wordList:
        for i in range(l):
            temp = word[:i] + '_' + word[i + 1:]
            # print(word)

            # print(temp)
            dic[temp].append(word)
    pprint.pprint(dic)

    print("--------- 上面全部是准备工作 ----------")
    # ---- 上面全部是准备工作 -----

    q1 = deque([beginWord])
    dis1 = {w: 0 for w in wordList}
    dis1[beginWord] = 1

    q2 = deque([endWord])
    dis2 = {w: 0 for w in wordList}
    dis2[endWord] = 1
    flag = True
    while q1 and q2:
        if flag:
            front, dis_front = q1, dis1
            back, dis_back = q2, dis2
        else:
            front, dis_front = q2, dis2
            back, dis_back = q1, dis1
        print('q1', q1)
        print('q2', q2)
        print('dis_front')
        print(dis_front)
        print('dis_back')
        print(dis_back)

        cur = front.popleft()
        dist = dis_front[cur]
        next_word = set([])
        print('-----cur-----')
        print(cur)

        for i in range(l):
            temp = cur[:i] + '_' + cur[i + 1:]
            sleep(1)
            print(temp)
            for w in dic[temp]:
                next_word.add(w)
            print(next_word)

        for w in next_word:
            sleep(5)
            print('word', w)
            if dis_back[w] > 0:
                return dist + dis_back[w]
            if dis_front[w] == 0:
                dis_front[w] = dist + 1
                front.append(w)
            print('q_head', dis_front)
            print('q_tail', dis_back)

        print('q1', q1)
        print('q2', q2)
        if len(back) < len(front):
            flag = not flag
        sleep(10)
    return 0


start = "hit"
end = "cog"
dict = ["hot", "dot", "dog", "lot", "log", "cog"]

print('result', ladderLength(start, end, dict))
