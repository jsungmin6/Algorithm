# # # # # # # # # # # # # # # # # # # # 1.
import sys
input = sys.stdin.readline


N,M=list(map(int,input().split()))
name1,name2=list(map(str,input().split()))



max_name_length=max(N,M)

str_list=[]
i=0
while i<max_name_length:
    if i<N:
        str_list.append(name1[i])

    if i<M:
        str_list.append(name2[i])
    i+=1

alpha={'A':3,'B':2,'C':1,'D':2,'E':4,'F':3,'G':1,'H':3,'I':1,'J':1,'K':3,'L':1,'M':3,'N':2,'O':1,'P':2,'Q':2,'R':2,'S':1,'T':2,'U':1,'V':2,'W':1,'X':2,'Y':2,'Z':1}

for i in range(len(str_list)):
    str_list[i]=alpha[str_list[i]]

while True:
    for i in range(len(str_list)-1):
        str_list[i]=(str_list[i]+str_list[i+1])%10

    del str_list[-1]
    if len(str_list)==2:
        if str_list[0]==0:
            print(str(str_list[1])+'%')
            break
        else:
            print(str(str_list[0])+str(str_list[1])+'%')
            break
    else:
        continue
