# https://programmers.co.kr/learn/courses/30/lessons/60060
# 3시 31분 시작

# 길이 10만, for문 돌릴수 있을 듯
# 모든 곳에 ? 포함되어있고, 접두사, 접미사에만 존재
#  양쪽에도 없으니까 일단 처음과 끝을 ? 있는지 체크하고 ?가 나오는 동안 체크하면 될 것 같네


# words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
words = ["min", "its", "m"]
queries = ["???", "mi?"]
# queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

def solution(words, queries):
    answer = []
    qdic  = {}
    for q in queries:
        ans = 0
        if q not in qdic:
            qlen = len(q)
            if q[0] == '?'and q[-1] == '?':
                for w in words:
                    wlen = len(w)
                    if wlen == qlen:
                        ans += 1
                        print("1")
                    elif wlen != qlen:
                        continue
            elif q[0] == '?':
                i = 0
                # 앞부분
                while  '?' == q[i]:
                    i+=1
                for w in words:
                    check = 0
                    for k in range(qlen-i):
                        if len(w)==qlen and w[qlen-k-1] == q[qlen-k-1]:
                            check += 1
                        else:
                            break
                    if check == qlen-i:
                        ans += 1
            elif q[-1] == '?':
                i = qlen-1
                while '?' == q[i]:
                    i -= 1
                for w in words:
                    check = 0
                    for k in range(i+1):
                        if len(w) == qlen and w[k] == q[k]:
                            check+=1
                        else :
                            break
                    if check == i+1:
                        ans +=1
            qdic[q] = ans
        else:
            ans = qdic[q]
        answer.append(ans)
    return answer
print("ans", solution(words,queries))