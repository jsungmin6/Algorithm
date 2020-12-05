from copy import deepcopy
import sys
t = int(input())
result=[]
 
for _ in range(t):
    cnd = []
    
    n = int(input())
    n_list = list(map(int,input().split()))
    c_n_list = deepcopy(n_list)
    answer = 5000000000000
    
    for i in range(len(n_list)-1):
        n_list[i] = n_list[i+1]
        if not n_list in cnd:
            cnd.append(n_list)
        n_list = deepcopy(c_n_list)
    
    for i in range(1,len(n_list)):
        n_list[i] = n_list[i-1]
        if not n_list in cnd:
            cnd.append(n_list)
        n_list = deepcopy(c_n_list)
 
    for l in cnd:
        count = 0
        for i in range(n-1):
            count+=abs(l[i]-l[i+1])
        answer = min(answer,count)
    
    result.append(answer)
 
for i in result:
    print(i)
 