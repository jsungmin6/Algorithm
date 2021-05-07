'''
풀이

9:00 부터 +t 한시간 안에 가장 먼저 도착한 m명을 태우는 행위를 n번 반목한다.

최대 태울 수 있는 인원 total을 구한다. total = n*m 이다.

waiting 그룹을 초기화한다.
먼저 00:00 부터 9:00 까지 서있는 사람들을 넣는다.

total - len(waiting) 을 한게 0 이하라면 콘또한 이 waiting 그룹에 포함되어야 한다.

1이상이라면 버스를 1대씩 보내고
waiting그룹에서 m명 보내고, 다음 시간대 크루를 waiting에 추가한다.
total 에서는 m만큼 빼준다.

계속 0이하가 되는지 확인한다.

0이하가 되었다면 거기서 m위안에 들어야한다. total번째 녀석보다 1분 빠른게 답이다.

마지막버스까지 공간이 남는다면 마지막 버스 도착시간이 답이다.

'''
from collections import deque
n=10
t=60
m=45
timetable = ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]

def append_waiting(start,end,datetimes):
    global waiting
    while datetimes:
        if start <= datetimes[0] <= end:
            waiting.append(datetimes.popleft())
        else:
            break

waiting = deque([])

def solution(n, t, m, timetable):
    
    total = n*m
    times = []

    for time in timetable:
        H,M = time.split(":")
        minutes = int(H)*60 + int(M)
        times.append(minutes)

    times.sort()
    datetimes = deque(times)

    zero = 0
    end = 9*60

    append_waiting(zero,end,datetimes)

    print("waiting 시작 초기화 : ",waiting)

    call_arive = False
    call_time = 0

    for i in range(n):
        waiting_num = len(waiting)

        if waiting_num >= total:
            # 콜도 타야함.
            print("waiting : ",waiting)
            call_time = waiting[total-1] - 1
            call_arive = True
            break

        else:
            # 콜 안탐
            
            # waiting에서 m명만큼 비움
            for _ in range(m):
                if waiting:
                    waiting.popleft()
                else:
                    break
            
            # 가능인원 줄임
            total -= m

            #waiting에 다음 시간 추가

            start, end = end,end+t
            append_waiting(start,end,datetimes)

    
    if call_arive:
        
        h = str(call_time//60)
        m = str(call_time%60)

        if len(h) < 2:
            h = "0"+h
        if len(m) < 2:
            m = "0"+m
        return h+":"+m
    else:
        h = str(start//60)
        m = str(start%60)

        if len(h) < 2:
            h = "0"+h
        if len(m) < 2:
            m = "0"+m
        return h+":"+m


print(solution(n, t, m, timetable))