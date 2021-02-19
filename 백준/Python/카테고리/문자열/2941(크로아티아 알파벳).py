'''
풀이
count 함수 이용하면 될 듯
dz= 과 z= 은 겹치므로 z= 수에서 dz= 수를 빼준다.
'''

croatia=["c=","c-","dz=","d-","lj","nj","s=","z="]

S=input()
answer=0
total = len(S)
ch_dz=0
for c in croatia:
    cnt=S.count(c)
    if c == "z=":
        cnt-=ch_dz
    answer+=cnt
    total-=len(c)*cnt
    if c=="dz=":
        ch_dz += cnt
print(total+answer)