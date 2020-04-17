# https://programmers.co.kr/learn/courses/30/lessons/42748
def solution(array, commands):
    answer = []
    for x in range(len(commands)):
        i = commands[x][0]-1
        j = commands[x][1]
        k = commands[x][2]-1
        sarr = sorted(array[i:j])
        answer.append(sarr[k])
    return answer

'''
고수님들
1. i.j.k 통합 
for command in commands에서 
일단 i,j,k = command 로 가능하다는 점 

2. lambda와 map이면 한줄로 ;;;
return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

혹은
return [sorted(array[s-1:e])[i-1] for s, e, i in commands]


'''