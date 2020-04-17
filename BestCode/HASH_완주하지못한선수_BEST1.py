# https://programmers.co.kr/learn/courses/30/lessons/42576
# \김형준 , ii , 홍승현 , YoungHo Choi , 민홍 외 448 명\
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

