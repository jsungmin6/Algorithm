'''
총 컵홀더 수 
'''

N=int(input())
S=input()
i=0
cups=1
while i< N:
    if S[i] =='S':
        cups+=1
        i+=1
    elif S[i] =='L':
        cups+=1
        i+=2

if cups > N:
    print(N)
else:
    print(cups)
