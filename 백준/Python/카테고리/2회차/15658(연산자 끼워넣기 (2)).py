'''
풀이
모든 순열을 구해도 될 것 같다. -> 시간초과
백트래킹으로 풀이
'''
from itertools import combinations,permutations
import sys
input = sys.stdin.readline

def solve(arr,cur,t,idx):
    answer = cur
    if t == 0: #덧셈
        answer+=arr[idx]
    elif t == 1:
        answer-=arr[idx]
    elif t == 2:
        answer*=arr[idx]
    else:
        if answer < 0:
            answer = (abs(answer) // arr[idx])*(-1)
        else:
            answer//=arr[idx]
    return answer
        

N = int(input())
arr = list(map(int,input().split()))
temp = list(map(int,input().split()))
cnt = [0,0,0,0]
total = arr
max_answer = -10000000000
min_answer = 10000000000
def dfs(cur,count,idx):
    global cnt,max_answer,min_answer
    if count == len(arr):
        if cur > max_answer:
            max_answer = cur
        if cur < min_answer:
            min_answer = cur
        return

    for i in range(4):
        if cnt[i] < temp[i]:
            cnt[i]+=1
            result = solve(arr,cur,i,idx+1)
            dfs(result,count+1,idx+1)
            cnt[i]-=1


dfs(arr[0],1,0)
print(max_answer)
print(min_answer)
