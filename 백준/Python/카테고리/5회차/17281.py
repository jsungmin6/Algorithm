'''
순서

순서가 9를 모두 구한다.

구한 순서를 토대로 시뮬레이션을 돌린다.
'''
import itertools,sys

input = sys.stdin.readline
arr = [1,2,3,4,5,6,7,8]

p = itertools.permutations(arr, 8)

N = int(input())
mat = [list(map(int,input().split())) for i in range(N)]

def game(start,t,arr):
    out = 0
    score = 0
    b1,b2,b3 = 0,0,0
    while True:
        if out == 3:
            break

        if t[arr[start]] == 0:
            out+=1
        elif t[arr[start]] == 1:
            score+=b3
            b1,b2,b3 = 1,b1,b2
        elif t[arr[start]] == 2:
            score +=(b2+b3)
            b1,b2,b3 = 0,1,b1
        elif t[arr[start]] == 3:
            score += (b1+b2+b3)
            b1,b2,b3 = 0,0,1
        elif t[arr[start]] == 4:
            score += (1+b1+b2+b3)
            b1,b2,b3 = 0,0,0
        
        start = (start+1)%9
    return start, score

def solve(arr,mat):
    start = 0
    total = 0
    for t in mat:
        start, score = game(start,t,arr) # 몇 번쨰 선수, 선수 정보, 선수 순서
        total += score
    return total

answer = 0
for i in p:
    l = list(i)
    l.insert(3,0)
    answer = max(solve(l,mat),answer)

print(answer)
