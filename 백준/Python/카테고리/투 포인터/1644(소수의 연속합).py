'''
풀이
에라토스테네스의 체로 소수리스트를 구한다.
구해지는 모든 수소는 자연수의 집합이며, 연속된 소수의 합을 구하는 것이니 투포인터를 사용할 조건이 된다.
투 포인터를 사용해서 경우의 수를 구한다.

시간복잡도
소수리스트 구하기 : nlogn
투 포인터 : O(N)
= nlogn
'''

N=int(input())
is_prime = [1 for _ in range(N+1)]
primes=[]
for i in range(2,N+1):
    if is_prime[i]:
        primes.append(i)
        for j in range(i*i,N+1,i):
            is_prime[j]=0

s=0
e=1
answer=0
while e != len(primes)+1:
    # print("s,e :",s,e)
    total = sum(primes[s:e])
    # print("total :",total)
    if total < N:
        e+=1
    elif total > N:
        s+=1
    else:
        answer+=1
        s+=1
        e+=1
print(answer)

