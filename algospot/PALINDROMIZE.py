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

# original의 접미사이면서 reversed_str의 접두사인 문자열 길이의 최대길이를 구한다
#def maxOverlap(a,b)
#n = len(a)
#m = len(b)
# reversed에 대해서 getPartialMatch, 실패함수구하기
#pi = getPartialMatch(b)
## begin == matched == 0에서 부터 시작
#begin, matched = 0, 0
#while begin <n:


def maxOverlap(original, reversed_str):

for _ in range(int(input())):
    original = input()
    len_original = len(original)

    reversed_str = ''
    for i in range(len_original-1, -1, -1):
        reversed_str += original[i]

    # 핵심! 원래 문자열과 뒤집은 문자열을 합친 뒤, Suffix와 Prefix끼리 겹치는 만큼 빼면 가장 짧은 문자열

    print(len_original * 2 - maxOverlap(original, reversed_str))
