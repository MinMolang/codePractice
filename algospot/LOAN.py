#syh0466님 풀이

def decision(balance, m, c):
    for i in range(m):
#이자가 붙고 잔금에서 상환액을 뺀다
        balance = balance * (P/12/100+1) - c
    return balance < 0

#amount원을 연 이율 rates 퍼센트로 duratiom 개월 간 갚으려면
#한달에 얼마씩 갚아야 하는가
#불변조건
#lo원씩 값으면 남은 개월 안에 갚을 수 없다
#hi원씩 갚으면 남은 개월 안에 갚을 수 있다
def optimize():
    lo = 0; hi = 104166667
    mid = (lo + hi) / 2
    for _ in range(100):
        if decision(N, M, mid):
            hi = mid
        else:
            lo = mid
        mid = (lo + hi) / 2

    return (lo + hi) / 2


for _ in range(int(input())):
    data = input().split()
    N = float(data[0])
    M = int(data[1])
    P = float(data[2])
    # print(round(optimize(), 9))
    print(optimize())
