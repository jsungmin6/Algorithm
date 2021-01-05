'''
'(' 일때 cnt+=1
')' 일때 answer+1,cnt-=1
'()' 일때 answer+=cnt
'''

bars=input()

stack=[]
cnt=0
answer=0
for i in bars:
    if not stack:
        stack.append(i)
        if i=='(':
            cnt+=1
    elif stack[-1]=='(' and i ==')':
        stack.append(i)
        cnt-=1
        answer+=cnt
    else:
        stack.append(i)
        if i=='(':
            cnt+=1
        else:
            answer+=1
            cnt-=1

print(answer)


# 깔끔한 풀이
import sys

def solution(arrangement):
    arrangement = arrangement.replace('()', '0');
    temp = 0    # "("의 개수 = 현재 진행중인 막대기 개수
    answer = 0

    for i in arrangement:
        if i == "(": temp += 1
        elif i == "0": answer += temp
        else:
            temp -= 1
            answer += 1
    return answer

x = sys.stdin.readline().rstrip()
print(solution(x))
