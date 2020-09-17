x="polymath"

answer=1
for i in range(len(x)-1):
    if x[i] >= x[i+1] :
        answer+=1

print(answer)
