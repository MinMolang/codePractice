def solution(A):
    # write your code in Python 3.6
    #pre-process
    #1)make number be unique
    #2)sort
    a = list(set(A))
    a.sort()
    min = 1
    for c in a:
        if c==min:
            min+=1
    return min