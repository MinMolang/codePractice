# https://programmers.co.kr/learn/courses/30/lessons/17678


case = 5
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
if case ==3:
    n = 2
    t = 1
    m = 2
    timetable = ["09:00", "09:00", "09:00", "09:00"]
    #08:59
if case ==4:
    n = 1
    t = 1
    m = 5
    timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]
    #"00:00"
if case ==5:
    n = 1
    t = 1
    m = 1
    timetable = ["23:59"]
    #09:00
if case ==6:
    n = 10
    t = 60
    m = 45
    timetable = ["23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59"]
    #"18:00"
if case ==7:
    n = 10
    t = 60
    m = 10
    timetable = ["17:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
'''시간 - >int '''
def timechange(time):
    ftr = [60, 1]
    return sum([a * b for a, b in zip(ftr, map(int, time.split(':')))])

'''int - > 시간  '''
def timechange2(time):
    time = '{:02d}:{:02d}'.format(*divmod(time, 60))
    return time
def solution(n, t, m, timetable):
    #print(timechange("09:00"))  9 시는 540입낟ㅇ
    # n회 t분  m명의 사람들을 태운다.

    #1. 시간을 정수로 바꾸기
    timetable = list(map(timechange,sorted(timetable)))
    print('timetable ',timetable)
    answer = 0
    now = 0  # * 필요한 이유, 마지막보다 일찍 올 것인가, 아니면 마지막 버스시간에 올 것인가 처리해주기 위해서
    last = 0 # 마지막사람을 항상 save하고 있음
    #버스 도착
    #2. n 회의 기회
    for k in range(n):
        #3. t분의 시간이고, t분의 시간이전에 온 m명의 사람만 받을 것임
        now = m
        bustime = 540 + k*t # 버스의 시간  # k가 n의 역할을 하고 있음
        print('bustime',bustime)

        # 4. timetable 에서 bustime 이전에 온 사람들을 m 명 만큼 데리고 온다.
        for p in range(m) :
            if timetable and timetable[0]<=bustime:
                print("ji")
                last = timetable.pop(0)
                now-=1
                print('busttime & pop ', bustime, ": ",last )
                print("timetable", timetable)


    print("i am last ", last)
    if now >0:
        answer = timechange2(540+(n-1)*t)
    else:
        answer = timechange2(last -1)

    return answer

print(solution(n,t,m,timetable))

