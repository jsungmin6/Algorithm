'''
하나 혹은 두개씩 문자를 잘라 used 배열에 놓음. (1~50 이기 때문)
두 경우 모두 사용된 수일 경우 경로를 자름(백)
끝까지 갔을때 순서대로 된 수열일 경우 종료
'''

from collections import deque
import sys
N = input()
used = [False]*51
temp = []
result = []


def back(i):  # i번째 수가 들어왔을 경우

    if i == len(N):
        limit = max(temp)
        if False in used[1:limit+1]:
            return
        for k in temp:
            print(k, end=' ')
        exit()

    one = int(N[i])
    if i < len(N) and not used[one]:
        used[one] = True
        temp.append(one)
        back(i+1)
        used[one] = False
        temp.pop()

    if i < len(N)-1 and int(N[i:i+2]) <= 50 and not used[int(N[i:i+2])]:
        two = int(N[i:i+2])
        used[two] = True
        temp.append(two)
        back(i+2)
        used[two] = False
        temp.pop()

back(0)

