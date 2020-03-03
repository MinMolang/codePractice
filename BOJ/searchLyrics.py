# https://programmers.co.kr/learn/courses/30/lessons/60060
# 3시 31분 시작

# 길이 10만, for문 돌릴수 있을 듯
# 모든 곳에 ? 포함되어있고, 접두사, 접미사에만 존재
#  양쪽에도 없으니까 일단 처음과 끝을 ? 있는지 체크하고 ?가 나오는 동안 체크하면 될 것 같네


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]

queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

'''
result
[3, 2, 4, 1, 0]
'''
def solution(words, queries):
    answer = []

    for q in queries:
    #     string도 for 문이 가능하니까
        ans = 0
        qlen = len(q)
        if q[0] == '?':
            print("앞")
            i = 0
            while  '?' == q[i]:

                i+=1
            print(i) #예상 : 3 : 실제 4 +1 되었음
            for w in words:
                check = 0
                print("예상 :1 ", qlen - i)
                for k in range(qlen-i):  # 여기까지만 앞에서부터 체크하면됨
                    if len(w)==qlen and w[qlen-k-1] == q[qlen-k-1]:
                        check += 1
                    else:
                        break
                if check == qlen-i:
                    print("앞까지 모두 맞음 ")
                    ans += 1
        elif q[-1] == '?':
            print("뒤")
            i = qlen-1
            while '?' == q[i]:
                i -= 1
            print(i) # 예상 3 , 2, 3, 3  /2, 1 22 -1 되어있음
            for w in words:
                check = 0
                for k in range(i+1): # 여기까지만 앞에서부터 체크하면됨
                    if len(w) == qlen and w[k] == q[k]:
                        check+=1
                    else :
                        break
                if check == i+1:
                    print("뒤 모두 맞음 ")
                    ans +=1

        answer.append(ans)
    return answer


print("ans", solution(words,queries))