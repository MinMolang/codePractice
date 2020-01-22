def solution(A, K):
    # write your code in Python 3.6
    if not A:
        return A
    else:
        front = K%len(A)
        return A[-front:]+A[:-front]
