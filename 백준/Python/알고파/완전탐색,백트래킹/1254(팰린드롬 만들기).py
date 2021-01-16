'''
아이디어
완전탐색

풀이과정
전체에서 왼쪽 문자를 하나씩 빼가며 이미 내부에 팰린드롬이 형성되어 있는지 확인한다.
있다면 전체길이에서 빼여진 수를 더한게 답이다.


시간복잡도
N개의 길이 가 있다면 N-1번만 해보면 결과를 알 수 있다.
O(N)
'''

S=input()

l=len(S)

for i in range(l):
    target = S[i:l]
    if target == target[::-1]:
        print(l+i)
        break




