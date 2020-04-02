S = "{{20,111},{111}}"

def solution(s):
    # k = s.split(",")
    s = s.split('},{')
    space = {}
    for k in s:
        k = k.replace("{","")
        k = k.replace("}", "")
        z = k.split(",")
        for _ in z:
            if _ not in space:
                space[_] = 1
            else:
                space[_] += 1
    answer = sorted(space.items(), reverse=True, key=lambda item: item[1])
    answer = [int(x[0]) for x in answer]
    return answer

    '''
    space = {}
    no = ['{',',','}']
    # answer = []
    for _ in s:
        if _ not in no:
            if _ not in space:
                space[_] = 1
            else:
                space[_] +=1
    answer = sorted(space.items(),reverse=True, key= lambda item: item[1])
    answer = [int(x[0]) for x in answer]
    return answer
    '''
    pass
print(solution(S))

# sorted 출처: https://rfriend.tistory.com/473 [R, Python 분석과 프로그래밍의 친구 (by R Friend)]