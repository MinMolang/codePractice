
# # 입력
# 2
# 7
# 27 16 9 12 54 36 72
# 9 12 16 27 36 54 72
# 6
# 409 479 10 838 150 441
# 409 10 479 150 838 441

# # 출력
# 12 9 16 36 72 54 27
# 10 150 441 838 479 409

# 전위순서는 ROOT부터 시작
# 중위순서에서 ROOT를 찾고 ROOT 이전 방문은 왼쪽 노드, 이후 방문은 오른쪽 노드
# 후위순서는 왼쪽 노드 호출, 오른쪽 노드를 호출 그리고 나서 루트 번호를 출력

# 트리의 전위탐색 결과와 중위 탐색 결과가 주어질 대 후위 탐색 결과를 출력한다

# hyooo 님 풀이 참고
def printPostOrder(preorder, inorder):
    if len(preorder) == 0:
        return

    # 트리의 루트는 전위 탐색 결과로 부터 알 수 있다
    root = preorder[0]
    # 트리의 왼쪽 서브 트리의 크기는 중위 탐색 결과에서 루트의 위치를 찾아서 알 수 있다
    root_idx = inorder.index(root)

    #왼쪽과 오른쪽 서브트리의 순회 결과를 출력
    printPostOrder(preorder[1: root_idx+1],inorder[:root_idx])
    printPostOrder(preorder[root_idx+1:], inorder[root_idx+1:])

    print(root, end=' ')

import sys
for _ in range(int(input())):
    N = int(input())

    preorder = list(map(int, sys.stdin.readline().rstrip().split()))
    inorder = list(map(int, sys.stdin.readline().rstrip().split()))

    printPostOrder(preorder, inorder)
