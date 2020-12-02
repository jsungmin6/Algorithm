N = int(input())
f = []
for _ in range(N):
    f.append(int(input()))

max_f = max(f)

fibo = [1, 1]
for i in range(2, 10000000):
    c = fibo[i-1]+fibo[i-2]
    fibo.append(c)
    if c > max_f:
        break


for i in f:
    array = []
    temp = i
    while True:
        if temp == 0:
            break
        for j in range(len(fibo)):
            if fibo[j+1] > temp:
                temp -= fibo[j]
                array.append(fibo[j])
                break
    array = sorted(array)
    for i in array:
        print(i, end=' ')
    print()
