array=list(input())
table=[1, 0 ,0]
for i in array:
    if i=='A':
        table[0],table[1]=table[1],table[0]
    if i=='B':
        table[1],table[2]=table[2],table[1]
    if i=='C':
        table[0],table[2]=table[2],table[0]

print(table.index(1)+1)
