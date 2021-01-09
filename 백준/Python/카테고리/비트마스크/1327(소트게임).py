from collections import deque

# N,K = map(int,input().split())

N,K=map(int,input().split())
L=list(input().split())


visited=set()
q=deque([["".join(L),0]])


# data=list(map(int,input().split()))
# sortdata = sorted(data)
# ans = ''.join(list(map(str,sortdata)))
# visited=set()
# q=[[''.join(list(map(str,data))),0]]

cnt=-1
while q:
    node, c = q.pop()
    visited.add(node)
    tempL=list(node)

    if tempL==sorted(tempL):
        cnt=c
        break
    
    
    for i in range(0,N-K+1):
        # left = temp[0:i]
        # reverse_target = temp[i:i+K]
        # reverse_data= reverse_target[::-1]
        # right = temp[i+K:]

        # new_data=''.join(left+reverse_data+right)
        newL = list(tempL)
        targetL=newL[i:i+K]
        targetL.reverse()
        for j in range(K):
            newL[i+j]=targetL[j]
        newWord="".join(newL)
        if newWord not in visited:
            q.append([newWord,c+1])
print(cnt)
    


