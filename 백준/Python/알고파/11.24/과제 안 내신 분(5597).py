#과제 안 내신 분..?
'''
배열 만들고 채워넣고 없는 배열 출력
'''
s=[0]*31
for _ in range(28):
    i = int(input())
    s[i] = 1

for i,k in enumerate(s[1:]):
    if k==0:
        print(i+1)


