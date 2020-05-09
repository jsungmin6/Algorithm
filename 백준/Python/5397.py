testcase=int(input())

for _ in range(testcase):
    result=list()
    temp=list()
    data=input()
    for i in data:
        if i=='<':
            if result:
                temp.append(result.pop())
        elif i=='>':
            if temp:
                result.append(temp.pop())
        elif i=='-':
            if result:
                result.pop()
        else:
            result.append(i)
    result.extend(reversed(temp))
    print(''.join(result))
