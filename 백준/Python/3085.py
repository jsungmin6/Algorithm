#사탕게임 S4

#풀이 방법
#인접하는것을 하나 바꿔서 먹을수 있는 최대 개수를 구하는 문제
#1개 바꾸고 최대개수 구하고
#또 다른거 1개 바꾸고 최대개수 구하고..
#반복
#최대개수 찾는 함수 구함
#인접한 것 바꾸는 함수 구함

################################################################
N=int(input())
candybox=[]
maxCount=1
for _ in range(N):
    candybox.append(list(input()))

def countMaxCandy(array):
    global maxCount
    for i in range(N):
        count=1
        for j in range(N-1):
            if array[i][j]==array[i][j+1]:
                count+=1
                print(count)
            else:
                if maxCount<count:
                    maxCount=count
                count=1

        if maxCount<count:
            maxCount=count

        count=1
        for j in range(N-1):
            if array[j][i]==array[j+1][i]:
                count+=1
            else:
                if maxCount<count:
                    maxCount=count
                count=1
        if maxCount<count:
            maxCount=count

for i in range(N):
    for j in range(N-1):
        if candybox[i][j]!=candybox[i][j+1]:
            candybox[i][j],candybox[i][j+1]=candybox[i][j+1],candybox[i][j]
            countMaxCandy(candybox)
            candybox[i][j+1],candybox[i][j]=candybox[i][j],candybox[i][j+1]

        if candybox[j][i]!=candybox[j+1][i]:
            candybox[j][i],candybox[j+1][i]=candybox[j+1][i],candybox[j][i]
            countMaxCandy(candybox)
            candybox[j+1][i],candybox[j][i]=candybox[j][i],candybox[j+1][i]

print(maxCount)
