'''
풀이

스택을 통한 덧셈

스택 구조에 하나씩 push한다.

빈칸이라면 push
문자라면 숫자로 변환하고 push
숫자라면 앞에꺼 pop 후 곱하고 push

대괄호라면 그냥 푸쉬

닫는괄호라면 최근 여는괄호까지 다 pop 하고 다 더해주고 push

끝나면 stack 남은 수 다 더해줌

'''

s = input()

d = {
    "H" : 1,
    "C" : 12,
    "O" : 16
}

stack = []

for i in s:
    if i in d:
        stack.append(d[i])
    elif i == "(":
        stack.append(i)
    elif i == ")":
        temp = 0
        while True:
            p = stack.pop()

            if p == "(":
                break

            temp += p
        
        if temp == 0:
            continue
        else:
            stack.append(temp)
    else:
        n = stack.pop()
        temp = n*int(i)
        stack.append(temp)

print(sum(stack))