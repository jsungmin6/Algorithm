N = int(input())
scores = []
for _ in range(N):
    scores.append(int(input()))

answer = 0
for i in range(len(scores)-1, 0, -1):
    if scores[i] <= scores[i-1]:
        diff = scores[i-1]-scores[i]+1
        answer += diff
        scores[i-1] = scores[i]-1
print(answer)
