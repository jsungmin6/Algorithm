'''
풀이
구현문제, 시간문자열 처리
'''

lines=[
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
'2016-09-15 20:59:59.591 1.412s',
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
'2016-09-15 21:00:00.966 0.381s',
'2016-09-15 21:00:02.066 2.62s'
]

def check(start,times):
    cnt=0
    end = start+1000
    for i in times:
        if i[0] < end and i[1] >= start:
            cnt+=1
    return cnt

def solution(lines):
    times=[]
    for i in lines:
        y,time,T = i.split(' ')
        hh,mm,ss = time.split(':')
        T=float(T.replace("s",""))*1000
        end = (int(hh)*3600+int(mm)*60+float(ss))*1000
        start = end-T+1
        times.append([start,end])
    answer=1
    for i in times:
        answer = max(answer,check(i[0],times),check(i[1],times))
    return answer

print(solution(lines))