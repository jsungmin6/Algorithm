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

#주어진 배열의 인접한 배열 최대 개수 구하기.
def countMaxCandy(array):
    global maxCount
    for i in range(N):
        count=1

        #인접한 수가 바뀔때마다 count=1로 초기화 하고 바뀌는 시점 count가 maxCount보다 크면 maxCount를 count로 초기화
        for j in range(N-1):
            if array[i][j]==array[i][j+1]:
                count+=1
            else:
                if maxCount<count:
                    maxCount=count
                count=1

        #한 행이 전부 같은 문자일 경우 위의 조건문에 의해 maxCount가 갱신이 안된다. 여기서 따로 갱신해 줌.
        if maxCount<count:
            maxCount=count

        #같은 방식으로 열 처리 해줌.
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

#for문을 돌리다가 다른색을 만났을 경우 서로 자리를 바꿔주고 countMaxCandy함수를 실행하고 다시 원상복구 해줌.
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
