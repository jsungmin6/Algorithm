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

0이하가 되었다면 거기서 m위안에 들어야한다. m번째 녀석보다 1분 빠른게 답이다.

마지막버스까지 공간이 남는다면 마지막 버스 도착시간이 답이다.

'''
from datetime import datetime
n=1
t=1
m=5
timetable = ["08:00", "08:01", "08:02", "08:03"]

def solution(n, t, m, timetable):
    waiting = []
    total = n*m

    zero = datetime.strptime("00:00","%H:%M")
    end = datetime.strptime("09:00","%H:%M")


    for time in timetable:
        d_time = datetime.strptime(time,"%H:%M")
        if zero <= d_time and d_time <= end:
            waiting.append(d_time)

    print(waiting)
    answer = ''
    return answer


print(solution(n, t, m, timetable))