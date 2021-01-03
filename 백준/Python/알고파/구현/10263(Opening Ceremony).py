N = int(input())
bd = list(map(int,input().split()))
bd.sort()
cnt=0
N-=1
high = bd[N]
l = len(bd)
s=0
while True:
    if l > high:
        for i in range(s,N+1):
            bd[i]-=1
            if bd[i] == 0:
                l-=1
                s+=1
        high-=1
        cnt+=1
    else:
        l-=1
        N-=1
        high = bd[N]
        cnt+=1
    if l==0:
        break
    print(bd)

print(cnt)

#깔끔코드

n = int(input())
floor = list(map(int, input().split()))


floor.sort(reverse = True)

charge = 0
Height = 0


while len(floor) !=0 :
    
    index = len(floor)

    if floor[0]-Height > len(floor) :
        charge += 1
        floor.pop(0)
    else :
        charge += 1
        Height += 1
        while floor[index -1] - Height == 0 :  
            floor.pop()
            index -= 1
            if len(floor) == 0 :
                break
        
    
print(charge)