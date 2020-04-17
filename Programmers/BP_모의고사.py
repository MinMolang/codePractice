# https://programmers.co.kr/learn/courses/30/lessons/42840
# 완전탐색 > 모의고사

def solution(answers):
    anlen = len(answers)
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    andict = {}
    andict[1] = 0
    andict[2] = 0
    andict[3] = 0
    for x in range(anlen):
        if answers[x] == one[x%5]:
            andict[1]+=1
        if answers[x] == two[x%8]:
            andict[2]+=1
        if answers[x] == three[x%10]:
            andict[3]+=1

    it = max(andict[1],andict[2],andict[3])
    hi = [-1,andict[1],andict[2],andict[3]]
    answer = [ i for i, x in enumerate( hi ) if x == it ]
#enumerate 출처 : http://m.blog.daum.net/bioinf/6543752
    return answer

'''
고수들은  아래 방식으로 .. 

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]

'''