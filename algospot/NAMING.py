# 입력
# ababcabababa
# bcabab

#출력
# 2 4 9 18

def getPartialMatch(N):
    m = len(N)

    # KMP로 자기 자신 찾기
    # N을 N에서 찾는다 begin = 0 이면 자기 자신을 찾아버리니까 안된다
    begin, match = 1, 0

    # 비교할 문자가 N의 끝에 도달할 때까지 찾으면서 부분일치 모두 기록
    while (begin + matched < m):
        #