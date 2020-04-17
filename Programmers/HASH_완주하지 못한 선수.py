# https://programmers.co.kr/learn/courses/30/lessons/42576

from collections import Counter
def solution(participant, completion):
    answer = ''
    a,b = Counter(participant),Counter(completion)
    answer = a-b
    answer = list(answer.keys())
    return answer[0]

'''
<고수분들 조금 더 간결하게는>
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
    
<정확성만 okay 받은>
def solution(participant, completion):
    answer = ''
    for runner in participant:
        a,b = participant.count(runner),completion.count(runner)
        if a!=b:
            answer = runner
            break
    return answer

'''
