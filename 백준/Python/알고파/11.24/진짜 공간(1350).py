#진짜 공간

# 풀이 과정
'''
나눗셈 할 줄 아느냐.
'''
N= int(input())
size_list= map(int,input().split())
cluster = int(input())

answer = 0
for size in size_list:
    if size == 0:
        continue
    a,b = divmod(size,cluster)
    if b != 0:
        a+=1
    answer+= a*cluster

print(answer)


