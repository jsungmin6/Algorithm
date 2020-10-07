#구간 합 구하기4

#풀이방법
#누적합


N,M = map(int,input().split())
list=list(map(int,input().split()))

sumList=[0]
sum=0
for i in list:
    sum+=i
    sumList.append(sum)

for _ in range(M):
    i,j=map(int,input().split())
    print(sumList[j]-sumList[i-1])
