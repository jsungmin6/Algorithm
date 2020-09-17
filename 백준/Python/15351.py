print(ord("A")-64)
data="OTAKU LIFE"
answer=0
for i in range(len(data)):
    if data[i]==' ':
        continue
    else:
        answer+=ord(data[i])-64
if answer==100:
    print('perfect life')
else:
    print(answer)
