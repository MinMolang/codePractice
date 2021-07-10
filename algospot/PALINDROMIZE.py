# # 입력
# 3
# there
# amanaplanacanal
# xyz
#
# # 출력
# 7
# 21
# 5

# 코드 출처 : https://jaimemin.tistory.com/590

# N에서 자기 자신을 찾으면서 나타내는 부분일치를 이용하여 pi를 계산
# pi[i] = N[...i]의 접미사도 되고 접두사도 되는 문자열의 최대 길이

def getPartialMatch(N):
    m = len(N)
    pi = [0] * m

    # KMP로 자기 자신을 찾는다
    # N을 N에서 찾는다. begin = 0 이면 자기 자신을 찾아버리니까
    begin, matched = 1, 0

    #비교할 문자가 N의 끝에 도달할 때까지 찾으면서 부분 일치 모두 기록
    while begin + matched < m:

        #begin + matched에 있는 문자와 matched에 있는 문자 일치
        if N[begin + matched] == N[matched]:
            matched += 1
            pi[begin + matched - 1] = matched

        # 일치하지 않고
        else:
            # matched가 0인 경우 begin을 한칸 앞으로
            if matched == 0:
                begin +=1

            #matched가 0이 아니면
            else:
                #begin을 (matched - 일치하는 접미사/접수다의 길이)만큼 더한다
                begin  += (matched - pi[matched - 1])
                matched = pi[matched - 1]

    return pi

# original의 접미사이면서 reversed_str의 접두사인 문자열 길이의 최대길이를 구한다
def maxOverlap(original, reversed_str):
    n, m = len(original), len(reversed_str)

    pi = getPartialMatch(reversed_str)

    # begin = matched = 0에서부터 시작
    begin, matched = 0, 0

    while begin < n:

        # 만약 original 해당글자와 역순 해당글자가 같다면
        if matched < m and original[begin + matched] == reversed_str[matched]:
            matched +=1
            if begin + matched == n:
                return  matched

        # 글자가 같지 않으면 getPartialMatch와 동일하게
        else:
            if matched == 0:
                begin += 1

            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]

        return 0


for _ in range(int(input())):
    original = input()
    len_original = len(original)

    reversed_str = ''
    for i in range(len_original-1, -1, -1):
        reversed_str += original[i]

    # 핵심! 원래 문자열과 뒤집은 문자열을 합친 뒤, Suffix와 Prefix끼리 겹치는 만큼 빼면 가장 짧은 문자열

    print(len_original * 2 - maxOverlap(original, reversed_str))
