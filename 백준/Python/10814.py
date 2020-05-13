n=int(input());
array=[]
for i in range(n):
    temp=input().split(' ')
    array.append((int(temp[0]),temp[1]))

answer=sorted(array,key=lambda x:x[0])

for i in answer:
    print(i[0],i[1])



    
