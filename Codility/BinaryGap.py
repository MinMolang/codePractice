#https://app.codility.com/programmers/lessons/1-iterations/binary_gap/ "codility DeomoTest link
def solution(N):
    # write your code in Python 3.6
    max = 0
    ba = bin(N)
    zero =0 # count zero num
    for idx,val in enumerate(ba):
        # skip idx 01 (0b)
        if idx in [0,1]:
            continue
        # if 1, makes count zero 0, check max if 0, zero+=1
        if val == '1':
            if zero>max:
                #only save zero to max ,zero is bigger than max
                max = zero
            #init zero , it has to be after than save zero which is bigger than max
            zero = 0
        else:
            zero+=1
    return max
