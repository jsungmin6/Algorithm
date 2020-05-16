s=input()
f=input()
index=0
result=0
while len(s)-index>=len(f):
    if s[index:index+len(f)]==f:
        result+=1
        index+=len(f)
    else:
        index+=1
print(result)
