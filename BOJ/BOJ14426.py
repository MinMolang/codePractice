# https://www.acmicpc.net/problem/14426
# 접두사 찾기
#   trie 구현체 출처 : https://blog.ilkyu.kr/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-trie-%ED%8A%B8%EB%9D%BC%EC%9D%B4-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0
'''
5 10
baekjoononlinejudge
startlink
codeplus
sundaycoding
codingsh
baekjoon
star
start
code
sunday
coding
cod
online
judge
plus
'''
# 7
class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[
                char]  # 딕셔너리이고, 없으면 위에서 추가해줬으니까 확실히 있을 거고, 그래서 o라는  children에는  chr이라는 node가 들어있을 것이다.
        curr_node.data = string  # 반환할때, string으로 반환 , 역추적없이 구현하기 위해

    def starts_with(self, prefix):
        curr_node = self.head
        # result = []
        subtrie = None

        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
                subtrie = curr_node
            else:
                return None
        if subtrie == None:
            return False
        else:
            return True
        # queue = list(subtrie.children.values())
        #
        # while queue:
        #     curr = queue.pop()
        #     if curr.data != None:
        #         result.append(curr.data)
        #     queue += list(curr.children.values())
        #
        # return result

import sys

n, m = list(map(int, sys.stdin.readline().strip().split()))
ans = 0

trie = Trie()

for i in range(n):
    trie.insert(sys.stdin.readline().strip())
for j in range(m):
    if trie.starts_with(sys.stdin.readline().strip())==True:
        ans+=1
print(ans)