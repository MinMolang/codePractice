# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#66,
def solution(A):
    # write your code in Python 3.6
    dic = {}
    for a in A:
        if not a in dic.keys():
            dic[a]= True
        else:
            if dic[a]==False:
                dic[a]=True
            if dic[a]==True:
                dic[a]=False
    return [key for key, val in dic.items() if val == True][0]
Analysis summary