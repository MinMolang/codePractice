# # bfs
# # 너비탐색, 큐 사용
# #   1
# #  2 3
# #
# # 그래프 모양 출처 : https://cyc1am3n.github.io/2019/04/26/bfs_dfs_with_python.html
graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1

# 방문 결과 : [1, 3, 4, 5, 2, 6]
# 1
# 3 4
# 5 2 6

visited = [False] * len(graph_list.keys())

queue = []

queue.append(root_node)
visited[root_node - 1] = True # 인덱스 때문에 한 칸 앞으로

while queue:
    value = queue.pop(0) # 선입선출
    print('방문 : ', value)
    connected = graph_list[value]
    for item in connected:
        if visited[item - 1]:
            continue

        queue.append(item)
        visited[item - 1] = True



