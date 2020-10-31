# 본대 산책

# 풀이 방법

'''
인덱스가 따로 주어지지 않았으니 설계 해야 함.
DP= [1 0 0 0 0 0 0 0]  : 1초후 건물별로 갈 수 있는 경우의 수 인덱스를 만드는 아이디어가 중요
그리고 다시 1초 후에는 인접한 건물들의 경우의 수 만큼 덧셈을 해주면 된다.

0 : 정복과학관 , 1 2
1 : 전산관 ,  0 2 3
2 : 미래관 , 0 1 3 4
3 : 신양간 , 1 2 4 5
4 : 한경직기념관 , 2 3 5 7
5 : 진리관 , 3 4 6
6 : 학생회관 , 5 7
7 : 형남공학관 , 4 6
'''
D=int(input())
DP= [1,0,0,0,0,0,0,0]

def nxt(state):
    temp = [0 for i in range(8)]
    temp[0] = state[1] + state[2]
    temp[1] = state[0] + state[2] + state[3]
    temp[2] = state[0] + state[1] + state[3] + state[4]
    temp[3] = state[1] + state[2] + state[4] + state[5]
    temp[4] = state[2] + state[3] + state[5] + state[7]
    temp[5] = state[3] + state[4] + state[6]
    temp[6] = state[5] + state[7]
    temp[7] = state[4] + state[6]

    for i in range(8):
        temp[i] %= 1000000007
    return temp

for i in range(D):
    DP = nxt(DP)

print(DP[0]%1000000007)