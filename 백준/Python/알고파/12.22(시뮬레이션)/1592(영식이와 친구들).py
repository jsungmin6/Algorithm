N, M, L = map(int, input().split())

balls = [0]*N

balls[0] = 1
cnt = 0
target = 0
while True:
    cnt += 1
    # 공 받을사람 정하기
    if balls[target] % 2 == 0:
        target = (target+L) % N
    else:
        target = target-L+N if (target-L) < 0 else target-L
    # 공 받을사람 볼 개수 늘려주기
    balls[target] += 1
    # 볼 개수가 M인지 확인하기
    if balls[target] == M:
        break

print(cnt)
