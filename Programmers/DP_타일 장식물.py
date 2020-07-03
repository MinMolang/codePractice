# https://programmers.co.kr/learn/courses/30/lessons/43104
# DP_타일 장식물
# 1) 피보나치 수 구하기
# 2) 피보나치 수를 구할 때, 반복되는 연산은 메모를 통해 또 구하지 않는다.
# 3) 타일 장식물 둘레 본인은 fibo[N]*3+fibo[N-1]*3+fibo[N-2]로 구하였으나
#     fibo[N]*4+ fibo[N-1] 등 다양하게 점화식을 세울 수 있다.
def solution(N):
    memo = [0, 1]
    def fibonacci(N):
        if N <= 1:
            return N
        else:
            if len(memo) <= N:
                memo.append(fibonacci(N - 1) + fibonacci(N - 2))
                return memo[N]
            return memo[N]
    fibonacci(N)
    answer = memo[N]*3+memo[N-1]*3+memo[N-2]
    return answer