'''
풀이
list의 max 값을 찾은 후 에라토스 테네스의 체로 소수를 구해놓은 후
list의 인자가 소수리스트에 몇 개 있는지 구한다.

시간복잡도
에라토스테네스의 체 nlogn

'''

N=int(input())
data=list(map(int,input().split()))
max_data=max(data)
isPrime=[1 for i in range(max_data+1)]
isPrime[1]=0
for i in range(2,max_data+1):
    if isPrime[i]:
        for j in range(i*i,max_data+1,i):
            isPrime[j] = 0

cnt=0
# print("isPrime:",isPrime)
for i in data:
    if isPrime[i] == 1:
        cnt+=1
print(cnt)