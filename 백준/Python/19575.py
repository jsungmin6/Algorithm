data = [
'10 3',
'3 2',
'9 1',
'3 0'
]

N=3
x=3
temp = 10
for i in range(1,len(data)):
    A=int(data[i][0])
    temp = temp*N + A
    print(temp)

print(temp%1000000007)

for i in range(3):
    print(i)
