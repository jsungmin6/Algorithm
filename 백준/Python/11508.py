#모든 값을 다 저장
#3으로 나눠 몫을 알아냄 몫이 공짜로 먹을 수 있는 개수 임
#최대한 비싼것끼리 묶음 : 비싼것 순서대로 정렬 후 3 ,6, 9 ... 제거
#합

N=int(input())
data=[]

for i in range(N):
    data.append(int(input()))

data.sort(reverse=True)

print(data)
sum=0
for i in range(len(data)):
    if i%3 == 2 :
        continue
    sum+=data[i]
print(sum)
