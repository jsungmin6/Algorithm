P,K = map(int,input().split())



# def era_prime(N):
#     check, answer = [0 for i in range(N+1)],[]
#     for i in range(2, N+1):
#         if check[i] == 0:
#             answer.append(i)
#         else:
#             continue
#         for j in range(i*i, N+1, i):
#             check[j] = 1
#     return answer

# K_r = era_prime(K)

for r in K_r:
    if P%r == 0:
        print('BAD',r)
else:
    print('GOOD')