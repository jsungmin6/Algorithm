t = int(input())
answer =[]
for _ in range(t):
    n,m = map(int,input().split())
    n_list = list(map(int,input().split()))
    m_list = list(map(int,input().split()))

    count = 0
    for i in n_list:
        if i in m_list:
            count+=1
    answer.append(count)

for i in answer:
    print(i)

        