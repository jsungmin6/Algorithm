from collections import deque
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
map = deque(['?']*N)
datas = []
for _ in range(K):
    S,W = input().split()
    datas.append([int(S),W])

def right(q):
    temp = q.pop()
    return q.appendleft(temp)

for data in datas:
    
    S,W = data
    S%=N
    for _ in range(S):
        right(map)

    #중복일 경우 넘어감
    if map[0] == W:
        continue
    #? 가 아닐경우 다른 글자가 중복으로 같은 자리에 들어오려는 것. -> !
    if map[0] != '?':
        print('!')
        exit() 
    #만약 같은 글자가 다른 곳에 존재할 경우 -> !
    if W in map:
        print('!')
        exit()

    map[0]=W
    
    # print(map)

for i in map:
    print(i,end='')
    

