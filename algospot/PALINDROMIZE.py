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


# python 코드 참고 풀이 출처 : aka1yutas님

def palindromize(original):
    reversed = original[::-1]
    length = len(original)

    if original == reversed:
        print(length)
        return

    j = 0
    pi = [0] * length

    for i in range(1, length):
        while j > 0 and original[i] != reversed[j]:
            j = pi[j - 1]

        if original[i] ==  reversed[j]:
            j += 1
            pi[i] = j

    print(length * 2 - pi[length - 1])




import sys

for _ in range(int(input())):
    palindromize(sys.stdin.readline().strip())
