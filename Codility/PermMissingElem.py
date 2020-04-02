# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
# Gauss Sum
def solution(A):
    ans = 0
    for i in A:
        ans+=i
    sa = len(A)+1
    return sa*(sa+1)//2 - ans