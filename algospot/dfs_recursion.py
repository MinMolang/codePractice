# dfs
# 깊이탐색, 스택 사용
#   1
#  2 3
#
# 그래프 모양 출처 : https://cyc1am3n.github.io/2019/04/26/bfs_dfs_with_python.html
graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1

# 1
# 3 4
# 5
# 2 6

# 방문 결과 : 1 4 3 5 6 2 둘다됨
# 방문 결과 : 1 3 5 2 4 6 둘다됨

visited = [False] * len(graph_list.keys())

def dfs(item):
    visited[item - 1]  = True

    print('방문 : ', item)

    connected = graph_list[item]
    for item in connected:
        if not visited[item - 1]:
            dfs(item)


dfs(root_node)