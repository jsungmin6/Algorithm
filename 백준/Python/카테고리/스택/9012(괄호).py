N=int(input())
for _ in range(N):
    stack =[]
    S = list(input())
    ch = True
    for s in S:
        if s == '(':
            stack.append(s)
        else:
            if stack:
                stack.pop()
            else:
                ch=False
                break;
    if not ch:
        print('NO')
        continue
    if stack:
        print('NO')
        continue    
    print('YES')

