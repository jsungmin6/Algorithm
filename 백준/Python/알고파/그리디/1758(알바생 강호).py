N = int(input())
hs = []
for _ in range(N):
    hs.append(int(input()))

hs.sort(reverse=True)

answer = 0
for i in range(len(hs)):
    if hs[i]-i > 0:
        answer += hs[i]-i
    else:
        break

print(answer)
