
sensor =[1, 6, 9, 3, 6, 7]
k=2
sensor.sort()

print(sensor)
answer=list()
for i in range(1,len(sensor)):
    answer.append(sensor[i]-sensor[i-1])

for i in range(k-1):
    del answer[answer.index(max(answer))]
    print(answer)
