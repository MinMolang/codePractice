# https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/
import math
def solution(X, Y, D):
    # write your code in Python 3.6
    left = Y-X
    ans = math.ceil(left/D)
    return ans