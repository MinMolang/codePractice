# https://programmers.co.kr/learn/courses/30/lessons/60060
#   trie 구현체 출처 : https://blog.ilkyu.kr/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-trie-%ED%8A%B8%EB%9D%BC%EC%9D%B4-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0

# 10시 44 분 시작


# words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
# 답: 3 2 4 1 0
words = ["min", "its", "m"]
queries = ["???", "mi?"]
# queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
#
# 답 : 2,1


class Node(object):
    def __init__(self, key, data=None):
        self.key = key  # 글자 하나 ex)알파벳
        self.data = data  #  마지막 글자, flag
        self.children = {}


# trie 구조를 만들어야하고
# init 함수, add 함수, search 함수를 제작해야함
class Trie(object):
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None) # 역순 모체임, tail이라는 노드가 생긴거고, children에 줄줄이 들어가 있는 것

    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char] #딕셔너리이고, 없으면 위에서 추가해줬으니까 확실히 있을 거고, 그래서 o라는  children에는  chr이라는 node가 들어있을 것이다.
        curr_node.data = string #반환할때, string으로 반환 , 역추적없이 구현하기 위해

        curr_node2 = self.tail
        for char in reversed(string):
            if char not in curr_node2.children:
                curr_node2.children[char] = Node(char)

            curr_node2 = curr_node2.children[char]
        curr_node2.data = string  # 아마 이대로 해도 될 것임, 검색할 때도, reverse로 검색할 것이기 때문에



    def search(self, string):
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        if (curr_node.data != None):
            return True

    def starts_with(self, prefix,strlen):
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
            if curr.data != None and len(curr.data) == strlen:
                result.append(curr.data)
            queue += list(curr.children.values())

        return result

    def ends_with(self, suffix,strlen):
        curr_node = self.tail
        result = []
        subtrie = None

        # 트라이에서 suffix를 찾고
        # suffix의 첫번째 글자 노드를 subtrie로 설정

        for char in reversed(suffix):
            if char in curr_node.children:
                curr_node = curr_node.children[char]
                subtrie = curr_node
            else:
                return None

        # bfs로 suffix subtrie를 순회하면서
        # data가 있는 노드를(완전한 단어)를 찾는다.
        queue = list(subtrie.children.values())

        while queue:
            curr = queue.pop()
            if curr.data != None and len(curr.data) == strlen:
                result.append(curr.data)
            queue += list(curr.children.values())

        return result

def solution(words, queries):
    answer = []
    # 이번에는 words를 모두 trie에 넣어주는 작업이 필요한데
    trie = Trie()
    for str in words:
        trie.insert(str)

    qdic  = {}
    for q in queries:
        ans = 0
        if q not in qdic:
            # 이제 시작이쥬, queries가 없다면 이제 queries를 통해 search를 해줘야즁~~
            qlen = len(q)
            if q[0] == '?'and q[-1] == '?':
                # 앞뒤가 모두 같은 경우는 길이만 같다면 다 더할 수 밖에!
                for w in words:
                    wlen = len(w)
                    if wlen == qlen:
                        ans += 1
                        print("1")
                    elif wlen != qlen:
                        continue
            elif q[0] == '?':
                i = 0
                # 앞부분 , reverse로 키워드를 만들어줘야함, .... 이걸 시간 안에 푼다고?ㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎ
                # queries = [ "????o", "???ko"]

                while  '?' == q[i]:
                    i+=1
                print("앞 i", i)
                if not trie.ends_with(q[i:], qlen):
                    ans = 0
                else:
                    ans = len(trie.ends_with(q[i:], qlen))

            elif q[-1] == '?':
                # 뒷부분 # queries = ["fro??",
                # words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
                i = qlen - 1
                while '?' == q[i]:
                    i -= 1
                print("뒤 i",i)
                if not trie.starts_with(q[:i + 1],qlen):
                        ans = 0
                else:
                    ans = len(trie.starts_with(q[:i+1],qlen))


            qdic[q] = ans
        else:
            ans = qdic[q]
        answer.append(ans)
    return answer
print("ans", solution(words,queries))