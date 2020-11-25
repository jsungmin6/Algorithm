#앵그리 창영
'''
피타고라스
'''
N,W,H = map(int,input().split())
max_h = W**2+H**2
for _ in range(N):
    h = int(input())
    if h**2 <=max_h:
        print('DA')
    else:
        print('NE')
    

