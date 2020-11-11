#유레카 이론

'''
1.100~999 까지 후보를 만들고
2.후보를 지워나가면서 남은 수를 센다.
'''

lst = [1 for i in range(1000)]
for k in range(123,988):
    i=list(str(k))
    if i[0] == '0' or i[1] == '0' or i[2] == '0':
        lst[k] = 0
        continue
        
    if i[0] == i[1] or i[1] == i[2] or i[0] == i[2]:
        lst[k] = 0
        continue

N=int(input())
for _ in range(N):
    num, s, b = map(int,input().split())
    num = list(str(num))
    for k in range(123,988):
        i=list(str(k))

        if i[0] == '0' or i[1] == '0' or i[2] == '0':
            continue
        
        if i[0] == i[1] or i[1] == i[2] or i[0] == i[2]:
            continue

        i_s=0
        i_b=0

        for u in range(3):
            for v in range(3):
                if u==v and num[u] == i[v]:
                    i_s+=1
                if u!=v and num[u] == i[v]:
                    i_b+=1
        
        if s!=i_s or b!=i_b:
            lst[k] = 0

print(sum(lst)-135)
            
        

        



