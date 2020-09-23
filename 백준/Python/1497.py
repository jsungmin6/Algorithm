#기타콘서트 S2

#풀이 방법

#비트마스킹 사용
#기타의 조합이 1,2,3....N까지 가능
#for문을 통해 1부터 증가하다가 혹시 최대값이 나오면 종료
#최대값이 안나오면 for문 끝까지 돌려서 모든 기타 사용한게 정답
#비트마스킹은 & 로 해서 모든 배열이 1이 되었을 때가 최대임.

################################################################

N,M=map(int,input().split())
bitmask=list()
all='1'*M
x=2
for _ in range(N):
    guitar,array=input().split()
    array=array.replace('Y','1').replace('N','0')
    bitmask.append(array)

array=[]
for i in bitmask:
    answer=int(i,2) #2진법 변환
    array.append(answer)

from itertools import combinations

result=0
y_count=0
for i in range(1, len(array)+1):
    for j in list(combinations(array, i)):
        #print(j)
        answer=j[0]
        if len(j)==1:
            if bin(answer).count('1') > y_count:
                y_count=bin(answer).count('1')
                result=i
            if answer==int(all,2):
                print(1)
                exit()
        else:
            for k in j:
                #print(answer)
                answer=bin(answer|k)
                answer=int(answer,2)
                if y_count < bin(answer).count('1'):
                    y_count=bin(answer).count('1')
                    result=i
                if answer==int(all,2):
                    print(i)
                    exit()
if result==0:
    print(-1)
else:
    print(result)


#다른풀이 1

#!/usr/bin/env python3
from itertools import combinations

def one_bits_in_bitset(bitset: int) -> int:
    '''
    정수 bitset를 이진수로 표기했을 때, 1bit가 몇개나 나타나는지 알아내는 함수

    Examples:
      one_bits_in_bitset(0b00000000) = 0
      one_bits_in_bitset(0b10010000) = 2
      one_bits_in_bitset(0b11111111) = 8
    '''
    w = 0
    while bitset:
        w += 1
        bitset &= bitset - 1
    return w

# guitar_count: 기타의 수
guitar_count, _ = map(int, input().split())

# DATA[x]: x번째 기타가 칠 수 있는 노래를 비트셋으로 표현한것
#
# 입력이 아래와 같을 경우:
#     4 5
#     A YYYNN
#     B YYNNY
#     C NNNYY
#     D YNNNN
#
# DATA는 아래와 같음:
#     DATA = [
#       0b00111,
#       0b10011,
#       0b11000,
#       0b00001,
#     ] = [7, 19, 24, 1]
DATA = []
for i in range(guitar_count):
    _, param = input().split()
    DATA.append(sum(
        1 << n for n, x in enumerate(param) if x == 'Y'
    ))

number_of_songs = 0
number_of_guitars = -1
for count in range(1, guitar_count + 1):
    for combination in combinations(DATA, count):
        union = 0
        for n in combination:
            print(union)
            union |= n

        songs = one_bits_in_bitset(union)
        if songs > number_of_songs:
            number_of_songs = songs
            number_of_guitars = len(combination)

print(number_of_guitars)
