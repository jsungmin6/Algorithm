# 회의실 배정

'''
시간이 짧은 것부터 채워나가면 될 것 같다. => 배열의 크기가 너무 큼
끝나는 시간이 짧은 것부터 정렬해 나가면 된다. 시작과 끝이 같을 수 있으니 끝시간이 같을때는 시작시간을 오름차순으로 정렬한다.
'''


import sys
input = sys.stdin.readline
N = int(input())
times=[]
for _ in range(N):
    s,e = map(int,input().split())
    times.append([s,e])

times.sort(key=lambda x : (x[1],x[0]))

count=0
start=0
end=0
for time in times:
    s,e = time

    if end <= s:
        count+=1
        start=s;
        end=e;

print(count)

################### 내풀이 => 시간초과
# import sys
# input = sys.stdin.readline
# N = int(input())
# times=[]
# for _ in range(N):
#     s,e = map(int,input().split())
#     times.append([e-s,s,e])

# time_table=[0]*(2**31)
# count=0

# times.sort()

# for time in times:
#     s=time[1]
#     e=time[2]

#     if 1 in time_table[s:e]:
#         continue
    
#     count+=1
#     for i in range(s,e):
#         time_table[i]=1

# print(count)