#https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/ "codility CyclicRotation link"
#In history,There are 75 87 100 answers 
def solution(A, K):
    # write your code in Python 3.6
    if not A:
        return A
    else:
        front = K%len(A)
        return A[-front:]+A[:-front]
