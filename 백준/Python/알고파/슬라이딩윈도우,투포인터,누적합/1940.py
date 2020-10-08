#주몽

#풀이 방법

'''
투포인터 이용
두가지의 재료로 만든다고 함.
정렬해서 배열 양 끝을 left 정점 right 정점이라하고
더한값이
'''

# # # # # # # # # # # # # # # # # # # # # 내 풀이
import sys
N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
item_list=list(map(int,sys.stdin.readline().split()))
item_list.sort()


left=0
right=len(item_list)-1
answer=0
while left<right:
    sum = item_list[left]+item_list[right]

    if sum>M:
        right-=1
    elif sum<M:
        left+=1
    else:
        right-=1
        left+=1
        answer+=1
print(answer)


# # # # # # # # # # # # # # # # # # # # # 다른 사람 풀이
'''
sort 후 투포인터가 아니라 target에서 box의 값을 하나 빼고 나머지가 box에 있느냐로 판별
'''
import sys
f = sys.stdin.readline

n = int(f())
target = int(f())
box = set(map(int, f().split()))

cnt = 0
for i in range(n):
    x = box.pop()
    if target-x in box:
        cnt += 1

print(cnt)
