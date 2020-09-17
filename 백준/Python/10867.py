N=4
data="3 4 2 3 1 4 2 3 1 -2 -1 0"
data= list(map(int,data.split()))

data=list(set(data))
haha=list(sorted(data))

data= list(sorted([x for x in data if x < 0])) + sorted([x for x in data if x >= 0])

print(data)

for i in range(len(data)):
    if i == len(data)-1:
        print(data[i], end='')
        break
    print(data[i], end =' ')
