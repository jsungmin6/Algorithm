'''
FIFO 니까 q를 이용해서 중요도를 필터링 하면서 진행 하면 될 듯
'''
from collections import deque


def max_ch(r,printer):
    for i in printer:
        if r < i[1]:
            return False
    return True


T=int(input())
for _ in range(T):
    cnt=0
    N,M = map(int,input().split())
    ranks = list(map(int,input().split()))
    printer = deque([])
    for i,rank in enumerate(ranks):
        printer.append([i,rank])
    while True:
        # print('printer:',printer)
        r = printer[0][1]
        if max_ch(r,printer):
            temp = printer.popleft()[0]
            cnt+=1
            if temp == M:
                break
        else:
            printer.append(printer.popleft())
    print(cnt)


        #뽑을때마나 cnt+=1
        #뽑힌 i 가 M 일때 종료