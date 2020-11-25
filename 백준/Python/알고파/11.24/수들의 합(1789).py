# 수들의 합 
# 풀이 과정
'''
등차가 1인 등차수열 같다.
'''

N = int(input())

answer = 0
for i in range(1,4294967295):
    if i*(i+1)//2 > N:
        break
    else:
        answer+=1

print(answer)
    
