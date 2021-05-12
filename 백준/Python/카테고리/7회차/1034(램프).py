'''
풀이

dp[i][j] i번째 시도에 j램프를 눌렀을 때 켜져있는 최대 행 수

dp[i][j] = dp[i-2][j]

완벽하게 일치하는 행의 수를 찾는다

그 행의 1과 0의 수를 찾는다.


'''
from collections import defaultdict

N,M = map(int,input().split())
lamp = []

for _ in range(N):
    lamp.append(input())

K = int(input())
d = {}

for i in lamp:
    if d.get(i):
        d[i][0]+=1
    else:
        #존재 안하면 "01" : [총 개수, 0의 수 ]
        cnt = i.count("0")
        d[i] = [1,cnt]

result = []
for i in d.values():
    result.append(i)

result.sort(reverse=True)
answer = 0
for i in range(len(result)):
    light_num,zero = result[i]

    if K < zero:
        continue
    else:
        if (K - zero)%2 == 0:
            # print("light_num,zero : ",light_num,zero)
            answer = light_num
            break;
        else:
            continue
print(answer)

