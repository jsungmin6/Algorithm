array = list(map(int,input().split()));

while array != [1,2,3,4,5]:
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            array[i],array[i+1] = array[i+1],array[i]
            for i in array:
                print(i,end=' ')
            print()

#빠른 답
import sys

n = list(map(int, sys.stdin.readline().split()))

for i in range(1, len(n)):
    for j in range(len(n)-i):
        if n[j]>n[j+1]:
            n[j], n[j+1] = n[j+1], n[j]
            print(*n)