C=6
P=7
data=[2,1,1,1,0,1]
count=0
if P==1:
    for i in range(len(data)-3):
        if data[i]==data[i+1]==data[i+2]==data[i+3]:
            count+=1
    print(C+count)
elif P==2:
    for i in range(len(data)-1):
        if data[i]==data[i+1]:
            count+=1
    print(count)
elif P==3:
    for i in range(len(data)-2):
        if data[i]==data[i+1]==data[i+2]-1:
            count+=1
    for i in range(len(data)-1):
        if data[i]-1==data[i+1]:
            count+=1
    print(count)
elif P==4:
    for i in range(len(data)-2):
        if data[i]-1==data[i+1]==data[i+2]:
            count+=1
    for i in range(len(data)-1):
        if data[i]==data[i+1]-1:
            count+=1
    print(count)
elif P==5:
    for i in range(len(data)-2):
        if data[i]==data[i+1]==data[i+2]:
            count+=1

    for i in range(len(data)-1):
        if data[i]==data[i+1]-1:
            count+=1

    for i in range(len(data)-1):
        if data[i]-1==data[i+1]:
            count+=1

    for i in range(len(data)-1):
        if data[i]-1==data[i+1]==data[i+2]-1:
            count+=1
    print(count)
elif P==6:
    for i in range(len(data)-2):
        if data[i]==data[i+1]==data[i+2]:
            count+=1

    for i in range(len(data)-1):
        if data[i]==data[i+1]:
            count+=1

    for i in range(len(data)-2):
        if data[i]==data[i+1]-1==data[i+2]-1:
            count+=1

    for i in range(len(data)-1):
        if data[i]-2==data[i+1]:
            count+=1
    print(count)
elif P==7:
    for i in range(len(data)-2):
        if data[i]==data[i+1]==data[i+2]:
            count+=1

    for i in range(len(data)-1):
        if data[i]==data[i+1]:
            count+=1

    for i in range(len(data)-2):
        if data[i]-1==data[i+1]-1==data[i+2]:
            count+=1

    for i in range(len(data)-1):
        if data[i]==data[i+1]-2:
            count+=1
    print(count)
