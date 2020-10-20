#비밀 지도

#풀이 방법

'''
비트 연산자 or 사용
이후 n자리수 만큼 0을 왼쪽 패딩으로 추가
1은 #으로 0은 ' ' 으로 처리

'''

# # # # # # # # # # # # # # # # # # # # #
def solution(n,arr1,arr2):
    maps=[]
    for i in range(n):
        #OR 연산 후 이진수 변환
        maps.append(bin(arr1[i]|arr2[i])[2:]
            .zfill(n)
            .replace('1','#')
            .replace('0',' ')
        )
    return maps
