# https://programmers.co.kr/learn/courses/30/lessons/42840
# 완전탐색 > 모의고사
# 전복오리백숙 , kimjooeun , 김영석 , ksmpooh , JB 외 55 명
def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]