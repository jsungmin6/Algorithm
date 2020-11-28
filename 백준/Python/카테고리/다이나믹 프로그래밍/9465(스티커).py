'''
전에 한 선택이 다음 선택에 영향을 준다.
탐욕법은 아니므로 다이나믹 프로그래밍으로 접근한다.
'''
#top down
# import sys
# sys.setrecursionlimit(100000)
# T = int(input())

# def sticker(c,status):
#     if c == n:
#         return 0
#     if dp[c][status] != -1:
#         return dp[c][status] #이미 계산
        
#     result = sticker(c+1,0); # 아무것도 안때고 넘어간다.
#     if status != 1: # 위의 스티커를 때는 것은 전에 안 땟을때와 아래꺼를 땟을 때 작동해야 함.
#         result = max(result,sticker(c+1,1) + stickers[0][c]); #아무것도 안땟을 때의 결과와 위에것을 땟을 때 이후의 결과 + 현재 위의것 가중치 중 큰것을 선택
#     if status != 2: # 아래 스티커를 때는 것은 전에 안 땟을때와 위에꺼를 땟을 때 작동해야 함.
#         result = max(result,sticker(c+1,2) + stickers[1][c]); #아무것도 안땟을 때의 결과와 위에것을 땟을 때 결과와 아래것을 땟을 때 이후의 결과 + 현재 아랫것 가중치 중 큰것을 선택
#     dp[c][status] = result;
#     return result;

# for _ in range(T):
#     n = int(input())
#     stickers = [list(map(int,input().split())) for i in range(2)]
#     dp = [[-1,-1,-1] for i in range(n+1)]

#     print(sticker(0,0))

#bottom up

T = int(input())
for _ in range(T):
    n = int(input())
    stickers = [list(map(int,input().split())) for i in range(2)]
    dp = [[0,0,0] for i in range(n+1)]

    for i in range(n):
        dp[i+1][0] = max(dp[i+1][0],dp[i][0],dp[i][1],dp[i][2])
        dp[i+1][1] = max(dp[i+1][1],max(dp[i][0],dp[i][2]) + stickers[0][i])
        dp[i+1][2] = max(dp[i+1][2],max(dp[i][0],dp[i][1]) + stickers[1][i])
    
    print(max(dp[n][0],dp[n][1],dp[n][2]))

##다른사람 풀이.

def solution(sticker):

    row = len(sticker[0])

    # a 위에 뗐을 때, b 아래 뗏을 때, c 둘다 안 뗏을 때
    a = b = c = 0
    for i in range(row):
        a, b, c = max(b, c) + sticker[0][i], max(a, c) + sticker[1][i], max(a, b)

    return max((a, b, c))


if __name__ == "__main__":

    loop = int(input())

    for ii in range(int(loop)):
        sticker = []
        row = input()
        for kk in range(2):
            sticker.append(list(map(int, input().split())))
        print(solution(sticker))


    



        
    