'''
분류
우선순위 큐

근거
절대값 힙, 작은수부터 출력해 배열에서 제거

풀이과정
1.절대값이 가장 작은 값을 출력 하는데 같을경우에는 -를 출력한다.
힙을 튜블로 저장해서 -,+ 여부를 파악하고 순서를 줘야할 것 같다.
2.다른 풀이를 보니 우선순위큐를 두개써서 음수와 양수를 나누어 저장해 깔끔하게 구했다.

시간복잡도
우선순위 큐는 삽입과 삭제가 O(log(N)) 이다 . N번 수행하니
O(Nlog(N))
'''
import heapq
import sys
input = sys.stdin.readline

N=int(input())
heap=[]
for _ in range(N):
    data = int(input())
    if data == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap,(abs(data),data))

#우선순위 큐 두개사용
import sys
import heapq
inp=sys.stdin.readline
n=int(inp())
hp=[]
hn=[]
for _ in range(n):
    x=int(inp())
    if x==0:
        if hp and hn:
            if hp[0]<hn[0]:
                print(heapq.heappop(hp))
            else:
                print(-heapq.heappop(hn))
        elif hp:
            print(heapq.heappop(hp))
        elif hn:
            print(-heapq.heappop(hn))
        else:
            print(0)
    else:
        if x>0:
            heapq.heappush(hp,x)
        else:
            heapq.heappush(hn,-x)