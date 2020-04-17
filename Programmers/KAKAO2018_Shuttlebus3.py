# https://programmers.co.kr/learn/courses/30/lessons/17678

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
    chance = n*m # 코은 chance-1에 타야한다.
    timetable = list(map(timechange,sorted(timetable)))
    print(timetable)
    lasttime = 0
    now = 0
    for k in range(n):
        now = m
        bustime = 540 + k*t
        for him in timetable:
            if now > 0 and him <= bustime:
                last = timetable.pop()
                now-=1
    print(now)
    print(last)
    if now >0:
        answer = timechange2(now)
    else:
        answer = timechange2(now-1)

print(solution(n,t,m,timetable))




