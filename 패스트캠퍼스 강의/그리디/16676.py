# 근우의 다이어리 꾸미기

# 풀이 방법

'''
스티커 1개 10까지 가능
스티커 2개 110 까지 가능
스티커 3개 1110 까지 가능
'''
N=int(input())

answer=1
for i in range(100):
    answer+=1
    limit = int('1'*int(answer))
    if N < limit:
        print(answer-1)
        break