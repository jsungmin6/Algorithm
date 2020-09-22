#시간표 짜기 S2

#풀이방법

#일단 비트 마스크 쓰지 않고 리스트로 만들어서 for문 돌리며 풀어보자

######################

N=int(input())
timeTable=[]
for _ in range(N):
    time=list(map(int,input().split()))
    timeTable.append(time[1:])

M=int(input())


for _ in range(M):
    st=list(map(int,input().split()))
    count=0
    for i in timeTable:
        data=set(i)-set(st)

        if list(data)==[]:
            count+=1
    print(count)
    count=0
