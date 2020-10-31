# 뒤집기

# 풀이 방법

'''
그리디는 한번 시행한 결과를 다시 하지 않는다.
감으로 푸는 경우가 많다.
규칙성 찾기
'''
str =input()
count=0
for i in range(len(str)-1):
    if str[i]!=str[i+1]:
        count+=1

print((count+1)//2) 