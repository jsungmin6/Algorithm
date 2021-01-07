'''
스택에 들어갈때 튜플로 들어감
하나씩 스택에 들어가는데 stack 에 들어가면서 자기보다 작은값은 다 제거 한다.
큰값을 만나면 list의 큰값의 순서를 넣고 없다면 0을 넣는다.
'''

N=int(input())
tops=[]
answer=[]
for i,h in enumerate(list(map(int,input().split()))):
    if not tops:
        tops.append((i+1,h))
        answer.append(0)
    elif tops[-1][1] < h:
        while tops[-1][1] < h:
            tops.pop()
            if not tops:
                tops.append((i+1,h))
                answer.append(0)
                break
            if tops[-1][1] >= h:
                answer.append(tops[-1][0])
                tops.append((i+1,h))
                break
    else:
        answer.append(tops[-1][0])
        tops.append((i+1,h))
        

print(*answer)


    
##깔끔
if __name__ =="__main__":
    tc = int(input())
    top = list(map(int, sys.stdin.readline().split())) #공백으로 분리
    s = []
    result = [0] * tc

    for i in range(tc):
        t = top[i]
        while s and top[s[-1]] < t:
            s.pop()
        if s:
            result[i] = s[-1] + 1
        s.append(i)

    print(' '.join(list(map(str, result))))
    ## (6,1) (9,2) (5,3) (7,4) (4, 4)

