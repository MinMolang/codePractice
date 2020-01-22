# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/ 
#Don't forget if continue,if continue or if elif
def solution(A):
    # write your code in Python 3.6
    dic = {}
    for a in A:
        if not a in dic.keys():
            dic[a]= True
        else:
            if dic[a] == True:
                dic[a] = False

            elif dic[a]==False:
                dic[a]=True


    return [key for key, val in dic.items() if val == True][0]
