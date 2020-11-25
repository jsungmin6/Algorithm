# 반올림
# 풀이 과정
'''
파이썬 round() 의 특이성 때문에 계속 틀림. round를 사용하지 않고 반오림을 수학으로 구현해야 함.
'''

k=10
a= int(input())
while a>k:
    if a%k < k/2:
        a = a-a%k
    elif a%k >= k/2:
        a = a-a%k
        a+=k
    k*=10;	
print(a)
    

