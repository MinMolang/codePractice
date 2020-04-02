# 스택 큐 사용하나요
# 시작 시간은 9시입니당
# n회 t분 m 명
# 한다면 큐를 왜냐하면 선입선출이기떄문ㅇ ㅔ
# 9시에도 가능
# 덱인가 ㅋㅋㅋ 가장 늦게 출발 시간 구해라
# 같은 시간 중에는 제일 뒤에
# 11:59분에는 집에 돌아가죵ㅇ
'''
n	t	m	timetable	answer
1	1	5	[08:00, 08:01, 08:02, 08:03]	09:00
2	10	2	[09:10, 09:09, 08:00]	09:09
2	1	2	[09:00, 09:00, 09:00, 09:00]	08:59
1	1	5	[00:01, 00:01, 00:01, 00:01, 00:01]	00:00
1	1	1	[23:59]	09:00
10	60	45	[23:59,23:59, 23:59, 23:59, 23:59, 23:59, 23:59, 23:59, 23:59, 23:59, 23:59, 23:59, 23:59, 23:59, 23:59, 23:59]	18:00

'''
case = 2
if case ==1:
    n = 1
    t = 1
    m = 5
    timetable = ["08:00", "08:01", "08:02", "08:03"]
if case ==2:
    n = 2
    t = 10
    m = 2
    timetable = ["09:10", "09:09", "08:00"]
# int - > str
def timechange(time):
    ftr = [60, 1]
    return sum([a * b for a, b in zip(ftr, map(int, time.split(':')))])

# str - > int
def timechange2(time):
    time = '{:02d}:{:02d}'.format(*divmod(time, 60))
    return time
def solution(n, t, m, timetable):
    # 내 생각에 일단 중요한 것은 무조건 timetable의 n*m-1에 위치하는 것
    # 예를 들어 5명까지 탈수있다. 1*5  을 일단 해준다. 노노 마지막 시간 -1일해주면 됨
    # if len(timetable)<=n*m:
    # #     작을 경우에는 무조건 그냥 마지막을 가져와버려
    #     ans = timetable[-1]
    # 버스를 중심으로 해야 겠따
    #
    bus = {540 : []}
    if n>1:
        for k in range(1,n):
            time = 540+k*t
            bus[time] = []

    print(bus)
    # while m>0:
    for _ in timetable:
        it = timechange(_)
        if it<=540:
            # m-=1
            bus[540].append(it)
            print(_)
        else:
            # 540 +t 550 +t  560+t  <720
            print(_,((it-540)//t)*t+540)
                # t로 나눈 다음 몫을 구하고 나머지를 버리면 됨
                # 그러면 버스 딕셔너리 어디인지 알 수 있음
                # max 회차 저장하기



    pass


print(solution(n,t,m,timetable))

