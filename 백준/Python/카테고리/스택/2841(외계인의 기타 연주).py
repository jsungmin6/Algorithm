import sys
input = sys.stdin.readline

N,P = map(int,input().split())
melody=[list(map(int,input().split())) for i in range(N)]
cnt=0
stack=[[] for i in range(N+1)]


for line,plat in melody:
    # print(stack)
    if not stack[line]: #스택이 비었으면 추가
        stack[line].append(plat)
        cnt+=1
    else:
        if plat == stack[line][-1]: #같은줄에 같은 플랫이 연속으로 오면 count 안함
            continue
        elif stack[line][-1] < plat:
            stack[line].append(plat)
            cnt+=1
        else:
            while True:
                stack[line].pop()
                cnt+=1
                if not stack[line]: #스택이 비면 종료 넣고 종료
                    stack[line].append(plat)
                    cnt+=1
                    break
                if stack[line][-1] < plat: # 빼다보니 크면 추가하고 count 하고 종료
                    stack[line].append(plat)
                    cnt+=1
                    break
                if stack[line][-1] == plat: #같으면 추가 안하고 count 안하고 종료
                    break
                
print(cnt)
#다른사람 풀이 : 배열에 0을 미리 넣어놓고 while문 조건을 이용해서 깔끔하게 해결함
import sys
input=sys.stdin.readline
N, P = map(int, input().split())
l=[[0],[0],[0],[0],[0],[0],[0]]
c=0
for i in range(0, N):
    n, p = map(int, input().split())
    while l[n][-1] > p:
        l[n].pop()
        c+=1
    if l[n][-1] != p:
        l[n].append(p)
        c+=1

print(c)








