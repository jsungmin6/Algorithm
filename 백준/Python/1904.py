def NChooseK_fast(n, k):
    numerator = 1
    denominator = 1
    k = min(n-k, k) #조합의 대칭성을 이용하여 더 적은 수의 연산을 하기 위해서입니다.
    for i in range(1, k+1):
        denominator *= i
        numerator *= n+1-i
    return numerator/denominator

N=4
count=0
list=[[i,N-2*i] for i in range(N//2+1)]
for i in list:
    answer=NChooseK_fast(i[0]+i[1],i[1])
    count+=int(answer)


print(count%15746)
