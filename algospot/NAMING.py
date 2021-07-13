
# 입력
# ababcabababa
# bcabab

#출력
# 2 4 9 18

# 코드 풀이 참고 // //출처: https://jaimemin.tistory.com/589#google_vignette [꾸준함]
def getPartialMatch(N):
    m = len(N)

    # KMP로 자기 자신 찾기
    # N을 N에서 찾는다 begin = 0 이면 자기 자신을 찾아버리니까 안된다
    begin, matched = 1, 0
    pi = [0] * m
    # 비교할 문자가 N의 끝에 도달할 때까지 찾으면서 부분일치 모두 기록
    while (begin + matched < m):
        # begin + matched에 있는 문자와 matched에 있는 문자 일치하는 경우
        if N[begin + matched] == N[matched]:
            matched += 1
            #pi : 실패함수
            pi[begin + matched -1] = matched

        # 일치하지 않고
        else:
            # matched 가 0 인경우 begin 을 한칸 앞으로
            if matched == 0:
                begin +=1
            else:
                # begin을  matched - 일치하는 접미사/ 접두사의 길이 만큼 더한다
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]

    return pi

# s의 접두사도 되고 접미사도 되는 문자열들의 길이 반환
def getPrefixSuffix(s):
    pi = getPartialMatch(s)
    k = len(s)
    result = []

    while k > 0 :

        #s[..k-1]는 답
        result.append(k)
        #s[..k-1]의 접미사도 되고 접두사도 되는 문자열도 답이다
        k = pi[k-1]
    return result

father = input()
mather = input()

combined = father + mather
result = getPrefixSuffix(combined)
result = list(map(str, result))
# 오름차순으로 출력하려면 역순으로 출력해야한다
print(' '.join(reversed(result)))
