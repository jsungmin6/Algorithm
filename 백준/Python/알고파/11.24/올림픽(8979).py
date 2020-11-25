# 올림픽 
# 풀이 과정
'''
정렬을 할 줄 아느냐
'''

N,k = map(int,input().split())
scores = [list(map(int,input().split())) for i in range(N)]


scores = sorted(scores,key=lambda x : (x[1],x[2],x[3]),reverse=True)

for i in scores:
    if i[0] == k:
        target = i
        break

answer=0
for score in scores:
    if score[1:] == target[1:]:
        answer += 1
        break
    else:
        answer +=1
print(answer)
