


def solution(a,b):
    answer  = 0
    it  = a*b
    bit = bin(it)
    for t in bit:
        if t=='1':
            answer+=1
    return answer

print(solution(1,1))
