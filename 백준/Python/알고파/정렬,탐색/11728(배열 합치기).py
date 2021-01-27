'''
내용
정렬

시간복잡도
nlogn
'''

N,B=map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = sorted(A+B)

print(*C)
