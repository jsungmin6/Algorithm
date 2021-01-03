import sys
input = sys.stdin.readline
result=[]
i=1
while True:
    t = input().rstrip().split()
    if t[0] == '0':
        break
    N=t[0]
    al=t[1]
    answer=[]
    for _ in range(int(N)):
        answer.append(input().rstrip())
    result.append('year {0}'.format(i))

    i+=1

    # print(answer)
    for p in range(len(answer)-1):
        for j in range(len(answer)-1):
            x,y = answer[j],answer[j+1]

            min_l = min(len(x),len(y))
            for k in range(min_l):
                if al.index(x[k]) > al.index(y[k]):
                    answer[j],answer[j+1] = answer[j+1],answer[j]
                    break
                elif al.index(x[k]) < al.index(y[k]):
                    break
                elif k==min_l-1:
                    if len(x)>len(y):
                        answer[j],answer[j+1] = answer[j+1],answer[j]

    for j in answer:
        result.append(j)

for i in result:
    print(i)
            

a=1
while 1:
    n=input();
    l=[]
    if n=='0':
        break
    n=n.split();
    p=n[1]
    for i in range(int(n[0])):
        l+=[input()]
    for i in range(len(l)-1):
        for k in range(len(l)-1):
            x,y=l[k],l[k+1];
            c=min(len(x),len(y))
            for j in range(c):
                if p.index(x[j])>p.index(y[j]):
                    l[k],l[k+1]=l[k+1],l[k]
                    break
                elif p.index(x[j])<p.index(y[j]):
                    break
                elif j==c-1:
                    if len(x)>len(y):
                        l[k],l[k+1]=l[k+1],l[k]
    
    print('year '+str(a),*l,sep='\n');a+=1