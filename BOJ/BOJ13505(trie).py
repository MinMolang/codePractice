# https://www.acmicpc.net/problem/13505
# 두 수 XOR
#   trie 구현체 출처 : https://blog.ilkyu.kr/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-trie-%ED%8A%B8%EB%9D%BC%EC%9D%B4-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0
'''
5
1 2 3 4 5
'''

# 5:55pm
class Node(object):
    def __init__(self, key, data=None):
        self.key = key  # 글자 하나 ex)알파벳
        self.data = data  # 마지막 글자, flag
        self.children = {}


# trie 구조를 만들어야하고
# init 함수, add 함수, search 함수를 제작해야함
class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]
        curr_node.data = string

    def search(self, string):
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        if (curr_node.data != None):
            return True

    def check(self, string):
        curr_node = self.head
        result = []
        subtrie = None
        dic = {'0':'1','1':'0'}
        for char in string:
            if dic[char] in curr_node.children:
                curr_node = curr_node.children[dic[char]]
                subtrie = curr_node
            else:
                return None
        queue = list(subtrie.children.values())
        print(queue)
        while queue:
            curr = queue.pop()
            if curr.data != None:
                result.append(curr.data)
            queue += list(curr.children.values())

        return result


    def starts_with(self, prefix):
        curr_node = self.head
        result = []
        subtrie = None

        # 트라이에서 prefix를 찾고
        # prefix의 마지막 글자 노드를 subtrie로 설정

        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
                subtrie = curr_node
            else:
                return None

        # bfs로 prefix subtrie를 순회하면서
        # data가 있는 도느들(완전한 단어)를 찾는다.
        queue = list(subtrie.children.values())

        while queue:
            curr = queue.pop()
            if curr.data != None:
                result.append(curr.data)
            queue += list(curr.children.values())

        return result

import sys
n = int(sys.stdin.readline().strip())
trie = Trie()
ans = 0

k = list(map(int, sys.stdin.readline().strip().split()))

for i in range(n):

    bin = format(k[i], 'b')
    if i == 0:
        trie.insert(bin)
    else:
        print("check",trie.check(bin))
        trie.insert(bin)


