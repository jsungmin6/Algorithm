'''
도착하는 지점이 빠른게 우선이다. 나중에 도착하는건 도착하는 지점이 빠른게 먼저 다 처리되고 계산되어야 한다.
1. 출발지부터 도착지 - 1 까지에서 트럭 잔여용량이 가장 적은 곳 찾기
2. 실을 박스의 수 정하기 (1에서 찾은 잔여용량보다 박스의 수가 많다면 1에서의 결과값만큼 박수 싣기)
3. 출발지부터 도착지 - 1 까지 실을 박수의 수만큼 잔여용량을 줄여주기
'''
import sys
input= sys.stdin.readline


N,C = map(int,input().split())
M = int(input())
box = []
for _ in range(M):
    box.append(list(map(int,input().split())))

boxs = sorted(box,key=lambda x : (x[1],x[0]))

record = [C]*(N+1)

total = 0
for box in boxs:
    s,e,n = box
    
    # 택배구간 중 현재 남은용량이 최소인 곳
    space = min(record[s:e])

    # 가능한 택배용량 총량에 더해주기
    temp = min(n,space)
    total += temp

    # 구간별 남는공간 업데이트
    if temp !=0:
        for i in range(s,e):
            record[i] -= temp

print(total)
    





