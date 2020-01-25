# https://programmers.co.kr/learn/courses/30/lessons/42889
# 실패율
# 2019-10-16
import operator
def dynamic(N,stages):
    s_list = [0]*(N+1)
    for num in stages:
        s_list[num-1]+=1
    before_sum = s_list[N]
    s_dict = dict()
    for i in range(N,0,-1):
        not_clear = s_list[i-1]
        stage_player = before_sum+not_clear
        before_sum = stage_player
        if before_sum == 0:
            s_dict[i] = 0.0
        else :
            s_dict[i] = not_clear/stage_player
    answer = []
    for dup in sorted(s_dict,key=lambda k:s_dict[k]):
        answer.append(dup)
    return answer
def solution(N, stages):
    pre_answer = dynamic(N,stages)
    answer = list(reversed(pre_answer))
    return answer
