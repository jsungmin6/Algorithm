#수리공 항승 S3

#풀이 방법

#가장 작은 수를 기준으로 테이프를 붙이기 시작한다.
#배열을 만들어 테이프가 붙여진 부분을 체크한다.
#체크되지 않은 부분 중 가장 작은 수를 기준으로 테이프를 붙인다.
#반복하며 구멍이 모두 막혔을 때까지 진행

################################################################

N,L = map(int,input().split())
spot=list(map(int,input().split()))
array=[0]*1001
count=0

while spot:
    node=spot.pop(0)
    if array[node]==0:
        count+=1
        for i in range(node,node+L):
            if i>1000:
                break
            array[i] = 1
print(count)
