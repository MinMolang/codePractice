def solution(A, K):
    # write your code in Python 3.6
    front = K%len(A)
    return A[-front:]+A[:-front]
