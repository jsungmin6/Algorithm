'''
풀이
에라토스테네스의 체를 사용해 한번 소수리스트를 만들어 놓고
모든 테스트케이스를 적용한다.

시간복잡도
nlogn
'''
import sys
input = sys.stdin.readline

max_test=250000
test=[]
while True:
    n=int(input())
    if n==0:
        break
    test.append(n)

isPrime=[1 for i in range(max_test)]
isPrime[1] = 0
for i in range(2,max_test):
    if isPrime[i]:
        for j in range(i*i,max_test,i):
            isPrime[j] = 0

for case in test:
    cnt=0
    for i in range(case+1,case*2+1):
        if isPrime[i] == 1:
            cnt+=1
    print(cnt)

    