'''
q를 만들어 이차원좌표를 넣어가면서 체크하면 될 듯
사과를 먹으면 그냥 append
사과를 안먹으면 append하고 popleft
좌표가 범위를 벗어나거나 이미 있는 좌표이면 죽음
'''

def find_direct(c_direct,C):#현재 방향과 C 주어지면 다음 방향 리턴함
    if c_direct == 'down':
        if C == 'L':
            next_di = 'right'
        else:
            next_di = 'left'
    elif c_direct == 'up':
        if C == 'L':
            next_di = 'left'
        else:
            next_di = 'right'
    elif c_direct == 'right':
        if C == 'L':
            next_di = 'up'
        else:
            next_di = 'down'
    else:#c_direct == 'left'
        if C == 'L':
            next_di = 'down'
        else:
            next_di = 'up'
    return next_di

def ch(i,j,dq): #주어지는 좌표가 가능한지
    #벽인지
    if i==N+1 or j == N+1 or i == 0  or j ==0:
        return False
    #뱀몸인지
    if [i,j] in dq:
        return False
    return True


import sys
from collections import deque
input = sys.stdin.readline
dq = deque([[1,1]])
N= int(input())
K= int(input())
apples=[]
for _ in range(K):
    i,j = map(int,input().split())
    apples.append([i,j])
L = int(input())
# print('apples : ',apples)
turns=[]
for _ in range(L):
    X,C = input().rstrip().split(' ')
    turns.append([int(X),C])

# print('turns : ',turns)

Map = [[0 for i in range(N+1)] for j in range(N+1)]

c_direct = 'right' #up down left right
c = [1,1]
cnt= 0
before_X = 0
for turn in turns:
    # print(turn)
    X,C = turn;
    t = X - before_X
    ci,cj = c #현재 위치좌표
    # print('출발 : {},{} 현재방향 : {} 다음 방향 : {} 몇번 가는지 : {}'.format(ci,cj,c_direct,C,t))
    for x in range(t):#dq에 좌표추가
        # print('dp : {} cnt :{}'.format(dq,cnt))
        cnt+=1
        if c_direct == 'down':
            ci+=1
            check = ch(ci,cj,dq) # 다음 들어올 좌표가 가능한지
            if not check:
                print(cnt)
                exit()
            dq.append([ci,cj]) # dq갱신
            if not [ci,cj] in apples: #사과좌표가 아니면 꼬리를 하나 자름
                dq.popleft()
            else:
                apples.remove([ci,cj])
        elif c_direct == 'up':
            ci-=1
            check = ch(ci,cj,dq) 
            if not check:
                print(cnt)
                exit()
            dq.append([ci,cj]) 
            if not [ci,cj] in apples: 
                dq.popleft()
            else:
                apples.remove([ci,cj])
        elif c_direct == 'left':
            cj-=1
            check = ch(ci,cj,dq)
            if not check:
                print(cnt)
                exit()
            dq.append([ci,cj]) 
            if not [ci,cj] in apples: 
                dq.popleft()
            else:
                apples.remove([ci,cj])
        else : # c_direct == 'right'
            cj+=1
            check = ch(ci,cj,dq)
            if not check:
                print(cnt)
                exit()
            dq.append([ci,cj]) 
            if not [ci,cj] in apples: 
                dq.popleft()
            else:
                apples.remove([ci,cj])
    before_X = X
    c=dq[-1]
    c_direct = find_direct(c_direct,C)#방향전환

    if turns[-1] == turn:
        for x in range(N+1):#dq에 좌표추가
            # print('dp : {} cnt :{}'.format(dq,cnt))
            cnt+=1
            if c_direct == 'down':
                ci+=1
                check = ch(ci,cj,dq) # 다음 들어올 좌표가 가능한지
                if not check:
                    print(cnt)
                    exit()
                dq.append([ci,cj]) # dq갱신
                if not [ci,cj] in apples: #사과좌표가 아니면 꼬리를 하나 자름
                    dq.popleft()
                else:
                    apples.remove([ci,cj])
            elif c_direct == 'up':
                ci-=1
                check = ch(ci,cj,dq) 
                if not check:
                    print(cnt)
                    exit()
                dq.append([ci,cj]) 
                if not [ci,cj] in apples: 
                    dq.popleft()
                else:
                    apples.remove([ci,cj])
            elif c_direct == 'left':
                cj-=1
                check = ch(ci,cj,dq)
                if not check:
                    print(cnt)
                    exit()
                dq.append([ci,cj]) 
                if not [ci,cj] in apples: 
                    dq.popleft()
                else:
                    apples.remove([ci,cj])
            else : # c_direct == 'right'
                cj+=1
                check = ch(ci,cj,dq)
                if not check:
                    print(cnt)
                    exit()
                dq.append([ci,cj]) 
                if not [ci,cj] in apples: 
                    dq.popleft()
                else:
                    apples.remove([ci,cj])

            
print(cnt)

