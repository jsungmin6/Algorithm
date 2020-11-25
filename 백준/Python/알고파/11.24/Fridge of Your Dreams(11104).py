#Fridge of Your Dreams
'''
그냥 이진수 변환
'''
N= int(input())

for _ in range(N):
    num = input()
    answer = 0
    for i in range(len(num)):
        answer += int(num[i]) * 2**(23-i)
    print(answer)


