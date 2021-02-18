'''
풀이
R,B,V 가 있다.
V 는 좌우에 있는게 같으면 안된다.
R,B,V는 같은게 연속으로 올 수 없다.
'''
N=int(input())
S=input()

top = S[0]
cnt=1
max_cnt=1
for i in S[1:]:
    if top == i or i == "V" or top =="V":
        max_cnt=max(cnt,max_cnt)
        cnt=1
        top=i
    else:
        cnt+=1
        top=i
        
max_cnt=max(cnt,max_cnt)
print(max_cnt)


