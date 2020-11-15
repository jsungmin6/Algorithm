# 멀티탭 스케줄링

'''
뒤에오는 전기용품이 얼마나 나중에 오는지 확인. 없다면 제일 먼저 빼버림.
'''


import sys
input = sys.stdin.readline
N,K = map(int,input().split())
datas = list(map(int,input().split()))
tab = []
count=0
for i,data in enumerate(datas) :
    if len(tab) != N and data not in tab:
        tab.append(data)
        continue
    
    if data in tab:
        continue
    
    idxs=[]
    for j in tab:
        try:
            idx = datas[i:].index(j)
        except:
            idx =101
        idxs.append(idx)
    
    out=idxs.index(max(idxs))
    del tab[out]
    tab.append(data)
    count+=1
print(count)

    




