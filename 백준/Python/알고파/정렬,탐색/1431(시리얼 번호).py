

N=int(input())
serial=[]
for _ in range(N):
    serial.append(input())

serial=sorted(serial,key=lambda x: (len(x),sum([int(i) for i in x if i.isdigit()]),x))

for i in serial:
    print(i)