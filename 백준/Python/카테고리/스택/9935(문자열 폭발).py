'''
풀이
폭발 문자열은 같은 문자를 두 개 이상 포함하지 않는다. 라는 조건이 전 선택이 다음 선택에 영향을 주지 못 하게 하는 장치를 한다.
일단 replace를 이용해 문자열로 문제를 해결해본다. => 시간초과
'''

s = input()
bomb = list(input())
stack = []
len_bomb = len(bomb)
for i in s:
    stack.append(i)
    if len(stack) >= len_bomb and stack[-len_bomb:] == bomb:
        for i in range(len_bomb):
            stack.pop()

print(''.join(ans) if stack else "FRULA")



##replace 활용 시간초과
# s = input()
# bomb = input()
# while s.find(bomb) != -1:
#     s = s.replace(bomb,"")
# if s:
#     print(s)
# else:
#     print("FRULA")

