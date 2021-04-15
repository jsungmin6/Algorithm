'''
풀이
그래프를 만들고 자식으로 부모에서 타깃으로 가는 간선을 끊은 후 리프노드의 수를 센다.
'''
from  collections  import deque
import sys
input = sys.stdin.readline

#리프노드 숫자 리턴한는 함수
def node_num(target,root):
    leef_num = 0
    q = deque([root])
    while q:
        node = q.popleft()

        if not graph[node]:
            leef_num+=1
        
        for nn in graph[node]:
            q.append(nn)
    return leef_num


N = int(input())
arr = list(map(int,input().split()))
rm = int(input())
graph = [[] for i in range(N)]
#부모 자식 그래프
root = -1
for i in range(N):
    if arr[i] == -1:
        root = i
        continue
    graph[arr[i]].append(i)

if rm == root:
    print(0)
    exit()

graph[arr[rm]].remove(rm) # 부모 -> 자식 간선 제거
print(node_num(rm,root))