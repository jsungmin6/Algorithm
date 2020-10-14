#친구비

#풀이 방법

'''
유니온파인드 find 와 merge 사용
나중에 인덱스가 필요하기에 uf 배열을 (1,-1) (2,-1) ... 이렇게 만듬
merge 로 다 연결하고
-1 을 값으로 가지고 있는게 부모임
부모 인덱스들을 for 문으로 돌려서 자식인덱스 들을 모아서 가장 작은값 찾아서 더해봄
더한게 가진돈보다 크면 Oh no 작으면 작은 값 출력
'''

# # # # # # # # # # # # # # # # # # # # # 내 풀이

#타고타고 올라가다가 결국 -1 인 녀석의 인덱스를 리턴함 = -1의 root를 리턴
def find(n):
    if (p[n][1] < 0):
        return n;
    p[n][1] = find(p[n][1]);
    return p[n][1]

#b가 a의 자식으로 들어감.
def merge(a,b):
    a=find(a);
    b=find(b);
    if(a==b):
        return
    p[b][1]=a;


import sys
input = sys.stdin.readline
N,M,K= map(int,input().split())
cost= list(map(int,input().split()))


p=[[i,-1] for i in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    merge(a,b)

# p[][1] == -1 이면 대가리이다. root_index_list에 대가리들을 모아준다.
root_index_list=[]
for i in p:
    if i[1]==-1 and i[0]!=0:
        root_index_list.append(i[0])

#그룹별 최소비용을 가진 녀석들을 찾아서 모아준다.
# group_cost=0
min_cost=sys.maxsize
# visited=[]

# find(1~N)까지 해서 root랑 같아지는 녀석들끼리 묶어서 min값찾고 group_cost에 넣어줌. 시간 오래 먹을듯.
# for root in root_index_list:
#     for i in range(1,N+1):
#         if i not in visited and find(i) == root:
#             min_cost=min(cost[i-1],min_cost)
#             visited.append(i)
#     group_cost+=min_cost
#     min_cost=sys.maxsize

index_list=[float('inf')]*(1+max(root_index_list))
for i in range(1,N+1):
    if find(i) in root_index_list:
        index_list[find(i)]=min(index_list[find(i)],cost[i-1])

group_cost=0
for i in root_index_list:
    group_cost+=index_list[i]

if group_cost<=K:
    print(group_cost)
else:
    print('Oh no')
