n=int(input());
array=[]
for i in range(n):
    array.append(list(input().split(' ')))

answer=sorted(array,key=lambda x:x[0])

for i in range(len(answer)):
    print(i)



    
