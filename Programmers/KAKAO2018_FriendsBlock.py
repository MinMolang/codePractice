# https://programmers.co.kr/learn/courses/30/lessons/17679
# 프렌즈블록

'''

m	n	board	answer
4	5	[CCBDE, AAADE, AAABF, CCBBF]	14
6	6	[TTTANT, RRFACC, RRRFCC, TRRRAA, TTMMMF, TMMTTJ]	15
'''

case = 2
if case ==1:
    n = 4
    t = 5
    m = ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']
    timetable = 14
if case ==2:
    n = 6
    t = 6
    m = ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']
    timetable = 15

# 와 탐색과 관련된 문제는 역시 너무 어렵다
# 일단, mn을 계속 탐색해야할지 모르겠꼬
# 중간에 pop 해서 빈캄을 없애야하니까
# 재귀로 계쏙 없애야 하는 거겟찌...??
def solution(m,n,board,answer):
    for i in range(m):
        for j in range(n):
            pass

    pass

print(solution(n,t,m,timetable))