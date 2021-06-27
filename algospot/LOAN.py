# 입력
# 4
# 20000000 12 6.8
# 35000000 120 1.1
# 40000000 36 0.5
# 100 120 0.1

# 출력
# 1728691.4686372071
# 308135.8967737053
# 1119696.7387703573
# 0.8375416659

# balance(C) : 매달 C 원씩 대출을 상환할 때 M개월 후의 대출 잔액을 balance (C)라 한다.
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

# hi = 100000000 * (1.0 + (50 / 12.0) / 100.0)
# hi = amounts max * (1.0 + (rates max / 12.0) / 100.0)
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
