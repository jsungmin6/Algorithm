'''
풀이
에라토스 테네스의 체
'''
M,N = map(int,input().split())

check, answer = [0 for i in range(N+1)], []

for i in range(2,N+1):
    if check[i] == 0:
        if i >= M: answer.append(i)
    else:
        continue
    for j in range(i*i, N+1,i):
        check[j] = 1

for i in answer:
    print(i)

# M,N = map(int,input().split())
# visit = [0]*(N+1)
# visit[0],visit[1] = 1,1
# for i in range(2,N+1):
#     if visit[i]: continue
#     for j in range(i*i,N+1,i):
#         visit[j] = 1

# for i in range(M,N+1):
#     if not visit[i]:
#         print(i)