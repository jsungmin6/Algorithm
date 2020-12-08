'''
스택으로 풀어본다
스택이 비었거나 top보다 현재 히스토그램 높이가 높다면, push한다.

스택의 top이 현재 히스토그램 높이보다 같거나 높다면, 그렇지 않게 될 때까지 pop한다. 이때 pop하면서 발생하는 각 직사각형의 넓이 중 최댓값이 결과가 된다.
[출처] 스택(Stack) (수정 2019-05-14)|작성자 라이
'''

N=int(input())
hitograms = []
stack=[]
result=[]
for _ in range(N):
    hitograms.append(int(input()))

for i,historgram in enumerate(hitograms):
    if not stack: # 스택이 비었으면 push한다.
        stack.append((i,historgram))
        continue
    
    if historgram > stack[-1][1]: # top보다 현재 히스토그램 높이가 높다면, push한다.
        stack.append((i,historgram))
        continue
    else: #스택의 top이 현재 히스토그램 높이보다 같거나 높다면, 그렇지 않게 될 때까지 pop한다
        while True:
            temp = stack.pop() # pop진행
            print('temp :',temp)
            if not stack:
                print('i :',i)
                size = i*temp[1]
                print('size :',size)
                result.append(size)
                break
            else:
                size = (i-temp[0])*temp[1] # 블록 크기 계산
                print('size :',size)
                result.append(size) #result에 블록 기록
            if historgram > stack[-1][1]:
                break
        stack.append((i,historgram))
    
    print('stack :',stack)
    if i == N-1:
        if stack:
            while True:
                temp = stack.pop() # pop진행
                print('temp :',temp)
                if not stack:
                    print('i :',i)
                    size = i*temp[1]
                    print('size :',size)
                    result.append(size)
                    break
                else:
                    size = (i-temp[0])*temp[1] # 블록 크기 계산
                    print('size :',size)
                    result.append(size) #result에 블록 기록
                if historgram > stack[-1][1]:
                    break


print(result)