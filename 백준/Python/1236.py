x,y=map(int,input().split())
array=[]

for _ in range(x):
    array.append(input())

row=[0]*x
column=[0]*y

for i in range(x):
    for j in range(y):
        if array[i][j]=='X':
            row[i]=1
            column[j]=1

rowcount=0
for i in range(x):
    if row[i]==0:
        rowcount+=1

columncount=0
for i in range(y):
    if column[i]==0:
        columncount+=1

print(max(rowcount,columncount))
