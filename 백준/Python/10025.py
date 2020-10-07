#게으른 백곰

#풀이방법

#슬라이딩 윈도우
#좌표를 배열인덱스로 생각하고 값들 넣어줌
#k*2+1 개가 윈도우로 생각하고 진행
#max값 갱신

################################################

N,k=map(int,input().split())
array=[0]*1000010
maxX=0
for _ in range(N):
    g,x=map(int,input().split())
    array[x]=g
    maxX=max(maxX,x)

window=k*2+1
left=0
right=left+window
maxAnswer=0

if maxX<=right:
    answer=sum(array)
    print(answer)
    exit(1)

while right<maxX+2:
    answer=sum(array[left:right])
    left+=1
    right+=1
    maxAnswer=max(maxAnswer,answer)

print(maxAnswer)
