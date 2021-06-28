from collections import deque


class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


a = DirectedGraphNode(0)
b = DirectedGraphNode(1)
c = DirectedGraphNode(2)
d = DirectedGraphNode(3)
e = DirectedGraphNode(4)
f = DirectedGraphNode(5)

a.neighbors = [b, c, d]
b.neighbors = [e]
c.neighbors = [e, f]
d.neighbors = [e, f]

test = [a, b, c, d, e, f]


def topSort0(graph):
    node_dict = {}

    for node in graph:
        node_dict[node] = 0

    for node in graph:
        for sub_node in node.neighbors:
            node_dict[sub_node] += 1

    q = deque([])

    for i in graph:
        if node_dict[i] == 0:
            q.append(i)

    res = []

    while q:
        pp(q)
        cur_node = q.popleft()

        if node_dict[cur_node] == 0:
            res.append(cur_node)

        for i in cur_node.neighbors:
            node_dict[i] = node_dict[i] - 1
            """
                如果这个地方写错了会导致重复计算
            """
            # if node_dict[i] == 0:
            #     q.append(i)
            q.append(i)
        # pp(res)
        print('dict')
        pdict(node_dict)
        print('--------------------------------')
    return res


def pp(arr):
    for i in arr:
        print('队列中', i.label)


def pdict(a_dict):
    for i in a_dict:
        temp = "key:" + str(i.label) + ' Value:'
        temp += str(i.label)
        temp += ' '

        print(temp)


topSort0(test)
