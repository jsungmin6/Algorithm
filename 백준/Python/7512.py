#연속하는 소수의 합
#소수 리스트를 구함. 10000000 전까지 구함
#3,5 라면 3개 연속되는 소수가 5개 연속되는 소수보다 큰 값들의 조합일 수 밖에 없다.
#가장 짧은 연속하는 소수를 소수리스트 인덱스를 1씩 증가시키면서 for문 돌림
#for 문 안에서 그다음 연속하는 수를 범위안에서 돌리며 같은 값을 가지는게 있는지 확인
#통과하면 true 그런식으로 모든 경우의 수 따짐

#에라토스테네스의 체 : 소수 리스트 구하는 방법
n=1000000
a = [False,False] + [True]*(n-1)
primes=[]
for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False


N=int(input())
answer=[]

for Scenario in range(N):
    m=int(input())
    nList=list(map(int,input().split()))

    #1개일 경우 바로 답 구해 준다.
    if len(nList)==1:
        result=0
        for i in range(nList[0]):
            result+=primes[i]
        answer.append(result)
    else:
        #많은 경우를 체크해 check=True 가 됐을때의 result값이 답이 되게끔 코드를 짬
        check=False;
        startIndex=max(nList)-min(nList)

        while check==False:
            result=0
            startIndex+=1
            temp=startIndex
            for i in range(min(nList)):
                result+=primes[temp]
                temp+=1

            for i in range(1,len(nList)):
                check=False
                S=startIndex
                E=startIndex+nList[i]
                Sum=sum(primes[S:E])
                while result<=Sum:
                    if Sum==result:
                        check=True;
                        break
                    S-=1
                    E-=1
                    Sum=sum(primes[S:E])
                if check==False:
                    break
            if check:
                break
        answer.append(result)

for i in range(N):
    print('Scenario ',i+1,':')
    print(answer[i])
    print()
