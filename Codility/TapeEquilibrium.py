# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/
# TapeEquilibrium

A = [-3,-1,-2,-3,  -3]

def solution(A):
    # write your code in Python 3.6

    size = len(A)
    #최초 1회는 ..
    lpoint = 1
    rpoint = size-2
    total = size -2
    left = A[0]
    right = A[-1]
    ans = 0
    print("s",A[lpoint], A[rpoint])
    while True:
        if  total==0:
            ans = abs(left-right)
            print("e",A[lpoint],A[rpoint])
            break

        elif left<=right:
            left += A[lpoint]
            print("r",left,right)
            total -=1
            lpoint+=1
        elif left>right:
            right += A[rpoint]
            print("l",left,right)
            total -= 1
            rpoint -= 1
    return ans


print(solution(A))