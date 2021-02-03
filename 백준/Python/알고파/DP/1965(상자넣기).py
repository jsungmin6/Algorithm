'''
앞에 자신보다 앞에 있었으면서 자신보다 작은 상자가 포함하고 있는 최대의 상자 개수를 가져와 +1만큼 하면 해당 상자에 상자들을 최대로 넣을 수 있는 상태가 된다.

출처: https://suri78.tistory.com/192 [공부노트]
'''

n = int(input())
box = list(map(int, input().split()))
size = [0] * 1001
for b in box:
    size[b] = max(size[:b]) + 1
print(max(size))
