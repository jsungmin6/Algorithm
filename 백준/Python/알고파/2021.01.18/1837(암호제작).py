'''
알고리즘

풀이과정

시간복잡도

'''

P,K = map(int,input().split())

def find_prim(N):
    check, answer = [0 for i in range(N+1)], []
    for i in range(2, N+1):
        if check[i] == 0:
            answer.append(i)
        else:
            continue
        for j in range(i*i, N+1, i):
            check[j] = 1
    return answer


K_r = find_prim(K-1)
for r in K_r:
    if P%r == 0:
        print('BAD',r)
        exit()
else:
    print('GOOD')