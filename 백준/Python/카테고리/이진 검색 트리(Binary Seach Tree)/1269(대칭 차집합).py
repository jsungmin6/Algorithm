'''
BTS 문제라고 함.
하지만 실제라면 set을 이용해서 구할 듯.
'''

num_a,num_b = map(int,input().split())
A=set(map(int,input().split()))
B=set(map(int,input().split()))
num_ab = len(A.intersection(B))
print(num_a+num_b-num_ab*2)