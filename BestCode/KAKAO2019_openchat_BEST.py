record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan","Enter pc5432 minji","Change pc5432 mindi","Leave pc5432"]


def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        #역시 딕셔너리를 사용했어야했어...특히 딕셔너리는 키의 마지막 값을 저장하니까...
        #만약에 첫번째 키워드가 enter나 change라면 
        if rr[0] in ['Enter', 'Change']:
            #namespace= {uid1234 : Muzi}이게 계속 업데이트 됨  
            namespace[rr[1]] = rr[2]

    for r in record:
        #첫번째 키워드가 Change가 아니라면, 즉 enter나 change라면
        if r.split(' ')[0] != 'Change':
        #id에 맞는 이름을 적고 들어왔습니다. 나갔습니다.를 붙여준다.
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer

print(solution(record))