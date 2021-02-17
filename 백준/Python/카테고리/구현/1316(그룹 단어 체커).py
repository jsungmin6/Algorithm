'''
풀이
stack을 만들어 top 과 같으면 스킵하고 다르면 넣는다.
다 끝나고 set을 해 숫자가 다르면 그룹단어가 아니고 같으면 그룹단어이다.

시간복잡도
stack = O(N)
set = O(N)
'''

N=int(input())
answer=0
for _ in range(N):
    word = list(input())
    stack = []
    for i in word:
        if not stack:
            stack.append(i)
        elif stack[-1] == i:
            continue
        elif stack[-1] != i:
            stack.append(i)
    if len(stack) == len(set(stack)):
        answer+=1
    
print(answer)
