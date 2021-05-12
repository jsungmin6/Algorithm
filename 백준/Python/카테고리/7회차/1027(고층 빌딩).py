'''
풀이

각각 빌딩에서 볼 수 있는 최대 빌딩의 수를 구한다.
빌딩 수가 50 이하이므로 이중포문을 돌려도 충분하다.

1. 빌딩에서 왼쪽을 볼때
- 빌딩 바로 왼쪽부터 왼쪽 끝까지 진행
- 기울기가 지속적으로 감소해야 한다.
- 최대로 작았던 기울기르 저장해놓고 그것보다 작은 기울기가 나왔을 때만 값을 추가한다.

2. 빌딩에서 오른쪽을 볼때
- 빌딩 바로 오른쪽부터 오른쪽 끝까지 진행
- 기울기가 지속적으로 증가해야 한다.
- 최대로 큰 기울기를 저장해놓고 그것보다 큰 기울기가 나왔을 때만 값을 추가한다.

'''

N = int(input())
bd= list(map(int,input().split()))

def left_view(i):
    line = 10000000000
    view = 0
    cur_idx = i-1
    while cur_idx >= 0:
        dx = i-cur_idx
        dy = bd[i] - bd[cur_idx]
        dydx = dy/dx

        if dydx < line:
            view+=1
            line = dydx
        cur_idx-=1
    return view

def right_view(i):
    line = -10000000000
    view = 0
    cur_idx = i+1
    while cur_idx < N:
        dx = cur_idx-i
        dy = bd[cur_idx] - bd[i]
        dydx = dy/dx

        if dydx > line:
            view+=1
            line = dydx
        cur_idx+=1
    return view

idx = 0
max_view = 0
for i in range(N):
    l = left_view(i)
    r = right_view(i)
    # print("=======")
    # print("빌딩 인덱스 :",i)
    # print("빌딩 왼쪽 :",l)
    # print("빌딩 오른쪽 :",r)
    total = l+r
    if max_view < total:
        max_view = total
        idx = i

print(max_view)