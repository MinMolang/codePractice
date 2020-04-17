# https://programmers.co.kr/learn/courses/30/lessons/42576
# 정승룡 , 김염소 , - , - , jehglee 외 9 명
# dictemp2 {-1227187468044676551: 'stanko', -5075067097175374929: 'mislav', 8894062460664200668: 'ana'}
def solution(participant, completion):
    temp = 0
    dic = {}
    for part in participant:
        print("hash,part",hash(part))
        dic[hash(part)] = part
        temp += int(hash(part))
    print("dictemp1",dic,temp)
    for com in completion:
        print("hashcom",hash(com))
        temp -= hash(com)
    print("dictemp2", dic, temp)
    print("dictemp",dic[temp])
    answer = dic[temp]
    return answer

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(solution(participant,completion))