# https://programmers.co.kr/learn/courses/30/lessons/42888
# 오픈채팅방
# 2019-10-15
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan","Enter pc5432 minji","Change pc5432 mindi","Leave pc5432"]

from collections import defaultdict
def list_duplicates(seq):
    tally = defaultdict(list)
    for i,item in enumerate(seq):
        tally[item].append(i)
    return ((key,locs) for key,locs in tally.items()
                            if len(locs)>1)
def text(key,name):
    if key=='E':
        return(str(name)+'���� �����Խ��ϴ�.')
    elif key=='L':
        return(str(name)+'���� �������ϴ�.')
def solution(record):
    pre_answer = []
    id_list = []
    change_list = []
    for i,words in enumerate(record):
        word = words.split(" ")
        pre_answer.append(word)
        if word[0][0] == 'C':
            change_list.append(i)
        id_list.append(word[1])
    for dup in sorted(list_duplicates(id_list)):
        last_idx = dup[1][-1]
        idx_list = dup[1]
        if len(pre_answer[last_idx])!=2:
            last_name = pre_answer[last_idx][2]
            for change in idx_list[:-1]:
                if pre_answer[change][0][0]!='C':
                    pre_answer[change][-1]=last_name

        else:
            last_idx = dup[1][-2]
            last_name = pre_answer[last_idx][2]
            for change in idx_list[:]:
                if pre_answer[change][0][0]!='C':
                    pre_answer[change][-1]=last_name
    answer = [text(x[0][0],x[-1]) for x in pre_answer if x[0][0]!= 'C']
    return answer
