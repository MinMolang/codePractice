# # 입력
# 3
# 3
# ba
# aa
# ab
# 5
# gg
# kia
# lotte
# lg
# hanhwa
# 6
# dictionary
# english
# is
# ordered
# ordinary
# this

# # 출력
# INVALID HYPOTHESIS
# ogklhabcdefijmnpqrstuvwxyz
# abcdefghijklmnopqrstuvwxyz

# wkkyu08 님 풀이 참고

import sys
adj, seen, order = [], [], []


def make_graph(words):
    global adj
    adj = [[0 for _ in range(26)] for _ in range(26)]
    for j in range(1, len(words)):
        i = j - 1
        length = min(len(words[i]), len(words[j]))
        for k in range(length):
            if words[i][k] != words[j][k]:
                a = ord(words[i][k]) - ord('a')
                b = ord(words[j][k]) - ord('a')
                adj[a][b] = 1
                break


def dfs(here):
    global seen, order, adj
    seen[here] = 1
    for there in range(len(adj)):
        if adj[here][there] and not seen[there]:
            dfs(there)
    order.append(here)


def topological_sort():
    global adj, seen, order
    m = len(adj)
    seen = [0 for _ in range(m)]
    order.clear()
    for i in range(m):
        if not seen[i]:
            dfs(i)
    order.reverse()
    for i in range(m):
        for j in range(i+1, m):
            if adj[order[j]][order[i]]:
                return []
    return order


for _ in range(int(input())):
    N = int(input())

    words = [sys.stdin.readline().rstrip() for _ in range(N)]
    make_graph(words)
    result = ''
    R = topological_sort()
    if not R:
        result = 'INVALID HYPOTHESIS'
    else:
        for res in R:
            res = chr(res + ord('a'))
            result += res

    print(result)

