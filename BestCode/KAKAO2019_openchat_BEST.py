record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan","Enter pc5432 minji","Change pc5432 mindi","Leave pc5432"]


def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'���� ���Խ��ϴ�.', 'Leave':'���� �������ϴ�.'}
    for r in record:
        rr = r.split(' ')
        #���� ��ųʸ��� ����߾���߾�...Ư�� ��ųʸ��� Ű�� ������ ���� �����ϴϱ�...
        #���࿡ ù��° Ű���尡 enter�� change��� 
        if rr[0] in ['Enter', 'Change']:
            #namespace= {uid1234 : Muzi}�̰� ��� ������Ʈ ��  
            namespace[rr[1]] = rr[2]

    for r in record:
        #ù��° Ű���尡 Change�� �ƴ϶��, �� enter�� change���
        if r.split(' ')[0] != 'Change':
        #id�� �´� �̸��� ���� ���Խ��ϴ�. �������ϴ�.�� �ٿ��ش�.
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer

print(solution(record))