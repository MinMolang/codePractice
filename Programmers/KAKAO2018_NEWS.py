# https://programmers.co.kr/learn/courses/30/lessons/17677
# 뉴스 클러스터링
'''
inter or uni  == 0 이 아니라 uni == 0 만 1
교집합 0 = 0이라는 사실
+
7.10번 test case는 합집합 더해줄 때, 코드 복붙하느라 실수
'''
from collections import Counter
import math
def solution(str1, str2):

    sstr1 = [str1[k:k + 2].lower() for k in range(len(str1) - 1) if str1[k:k + 2].isalpha()]
    sstr2 = [str2[k:k + 2].lower() for k in range(len(str2) - 1) if str2[k:k + 2].isalpha()]
    print(sstr1, sstr2)
    lstr1 = len(sstr1)
    lstr2 = len(sstr2)
    inter = 0
    uni = 0
    cnt1 = Counter(sstr1)
    cnt2 = Counter(sstr2)
    print(cnt1, cnt2)
    if lstr1 <= lstr2:
        for a, b in cnt1.items():
            if a in cnt2:
                it= cnt2.pop(a)
                inter+= min(b,it)
                uni+=max(b,it)
            else:
                uni+=b
        for x in cnt2.values():
                uni+=x
    else:
        for a, b in cnt2.items():
            if a in cnt1:
                it = cnt1.pop(a)
                inter+= min(b,it)
                uni+=max(b,it)
            else:
                uni+=b
        for x in cnt1.values():
            uni+=x
        print(cnt1)
    if uni==0:
        answer =1
    else:
        answer = inter/uni
    return math.floor(answer*65536)
