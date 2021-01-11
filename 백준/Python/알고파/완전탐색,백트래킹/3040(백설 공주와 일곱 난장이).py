from itertools import permutations

hats=[]
for _ in range(9):
    hats.append(int(input()))

for i in permutations(hats,7):
    if sum(i) == 100:
        for j in i:
            print(j)
        break

