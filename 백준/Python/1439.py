S=input()

key=S[0]
count=0
for i in S[1:]:
    if key!=i:
        count+=1
        key=i

print((1+count)//2)
