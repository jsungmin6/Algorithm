# And the Winner Is... Ourselves! S5

# 풀이 과정

# 문제 이해하는데 좀 걸림
# 시간이 중첩되고 문제 풀었을 때 지금가지 흘러간 시간 모두가 패널티라 생각
# 못 풀었을 때의 점수는 항상 같으니 더해줌

#####################################

answer=0
array=[]
for _ in range(11):
    D,V=map(int,input().split())
    array.append([D,V])

array.sort()
time=0
answer=0
for i in array:
    time+=i[0]
    answer+=time
    answer+=i[1]*20

print(answer)
