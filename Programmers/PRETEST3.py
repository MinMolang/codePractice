'''
1. 0, 1 패턴으로 만들지
2. 1, 0 패턴으로 만들지 결정해야하는데
3. 일단 그것만 결정하면 나머지는 바꾸고 count
어쩌면 0,1 패턴인지, 1,0 패턴인지는 안중요한게 아닐까
1 1 1
0 0 0 인덱스들을 모으고
짝수인덱스들 속에 홀수 인덱스
홀수 인덱스들 속에 짝수 인덱스 의 개수를 카운트할까?
0 0 0
(0) (2) (4)
1 1 1
(1) (3) (5)

101011
2진수여봐 ..
010100
올바른 형태의 경우는
0 1 1 0
zero = [

개수가 얼마 안되니까 그냥 앞뒤로 둘다 해봐도 될 듯
 # 0 1 0 1 0 1 검사
 # 1 0 1 0 1 0  검사
'''
def solution(a):
    zeropattern = 0
    onepattern = 0
    # 홀수인덱스 체크
    # zeropattern 시작패턴이면 0이 있어야한다.  0이 아니면 증가
    # onepattern이면 1이 있어야한다. 1이 아니면 증가
    for t in a[::2]:
        if t == 0:
            onepattern+=1
        else:
            zeropattern+=1
    # 짝수인덱스 체크
    # 0 1 0 1 0 1 검사
    # 1 0 1 0 1 0  검사
    # zeropattern 시작패턴이면 1이 있어야한다.  1이 아니면 증가
    # onepattern이면 0이 있어야한다. 0이 아니면 증가
    for t in a[1::2]:
        if t == 0:
            zeropattern += 1
        else:
            onepattern += 1
    answer = min(zeropattern,onepattern)
    return answer

A = [0,1,1,0]
Aa = 2

B = [0,1,0]
Ba = 0

C = [1,1,0,1,1]
Ca = 2

D = [1,0,1,0,1,1]
Da = 1
print(solution(D))