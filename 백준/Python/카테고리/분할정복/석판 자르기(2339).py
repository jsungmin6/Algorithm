#  석판 자르기

'''
먼저 리턴 할 수 있는 조건을 만든다.
이후 분할해서 문제를 해결한다.
'''


def division(startX,endX,startY,endY,Map,direction):
    # 분할된 Map 구역을 돌면서 보석수와 불순물 수를 센다.
    # 만약 보석수가 0 이라면 이 경우는 빼야 한다.
    # 보석수가 1개 있고 불순물이 0개라면 이건 하나의 경우의 수가 된다.
    starCount = 0
    impuritiesCount = 0
    for x in range(startX,endX):
        for y in range(startY,endY):
            if Map[y][x] == 2:
                starCount +=1
            elif Map[y][x] == 1:
                impuritiesCount +=1
    if starCount == 0:
        return 0
    elif starCount == 1 and impuritiesCount == 0:
        return 1

    
    #재귀문을 통해 답을 도출한다. 2가지 경우로 갈라졌다면 총 경우의 수는 첫번째와 두번째의 곱이다.
    #가로로 자른것은 다음에 세로로 잘라야 하기 때문에 direction을 넣어 구분해 주었다.
    answer = 0

    for x in range(startX,endX):
        for y in range(startY,endY):
            if Map[y][x] == 1:
                if direction != 0:      
                    answer += division(startX, x, startY, endY, Map, 0) * division(x + 1, endX, startY, endY, Map, 0);
                if direction != 1:
                    answer += division(startX, endX, startY, y, Map, 1) * division(startX, endX, y + 1, endY, Map, 1);

    return answer


N = int(input())
Map = [list(map(int,input().split())) for i in range(N)]

answer = division(0,N,0,N,Map,-1)

if answer == 0:
    print(-1)
else:
    print(answer)


