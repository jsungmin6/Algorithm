'''
내용
정렬 할 줄 아느냐

시간복잡도
nlonn
'''

W=[]
K=[]

for _ in range(10):
    W.append(int(input()))
    
for _ in range(10):
    K.append(int(input()))

W.sort(reverse=True)
K.sort(reverse=True)

print(sum(W[:3]),sum(K[:3]))
