# 1년전 풀이
def solution(n, t, m, timetable):
    # 1단계 timetable 오름차순 정렬
    timetable.sort()
    # 일단 m의 개수가 > timetable.legnth
    if m > len(timetable):
        # 아홉시 이전이면 무조건 9시 차를 탄다
        if timechange(timetable[-1]) <= 540:
            answer = 540
        else:
            answer = 540 + (n - 1) * t  # 아홉시 이후면 n회 계산에서 그 시간을 탄다. 예를 들어 6시
        return timechange2(answer)
    # 일단 n 이 1이 되었다고 가정, 나중에 반복문으로 바꿔야함

    seatcount = 0
    totalcount = 0
    # nowPeople = len(timetable)  # 현재 남은 사람들
    answer = 540
    # 밑에 n일지 n-1이 될 지 생각해보아야함
    y = 0

    for x in timetable:
        x = timechange(x)
        #큰지먼저 파악
        if (x > answer + y * t):
            y += 1
            seatcount = 0
        if x <= answer + y * t:
            seatcount += 1
        if seatcount==m and y<n:
            y+=1
            seatcount = 0

        if seatcount==m and y>=n :  # 차가 끝났습니다!
            answer = x
            break
        answer = x
    if answer > 540 + (n - 1) * t:
        answer = 540 + (n - 1) * t
    else:
        answer = answer - 1

    return timechange2(answer)


def timechange(time):
    ftr = [60, 1]
    return sum([a * b for a, b in zip(ftr, map(int, time.split(':')))])


def timechange2(time):
    time = '{:02d}:{:02d}'.format(*divmod(time, 60))
    return time