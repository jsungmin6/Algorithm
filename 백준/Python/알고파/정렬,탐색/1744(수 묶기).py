'''
풀이 방법
1. 정렬
2. 양수 x 양수
3. 음수 x 음수 
4. 양수 x 음수 불가
5. 음수 x 0 가능
6. 양수 x 0 불가
'''
import sys
input = sys.stdin.readline
N = int(input())

# if N==1:
#     print(int(input()))
#     exit(0)
minus = []
minus_num=0
plus = []
plus_num=0
ones=0
for i in range(N):
    num = int(input())
    if num > 1:
        plus.append(num)
        plus_num+=1
    elif num ==1:
        ones+=1
    else:
        minus.append(num)
        minus_num+=1

minus.sort()
plus.sort(reverse=True)

plus_sum=0
minus_sum=0



for i in range(0,plus_num//2):
    plus_sum+=plus[i*2]*plus[i*2+1]

if plus_num%2!=0 and plus:
    plus_sum+=plus[-1]

for i in range(0,minus_num//2):
    minus_sum+=minus[i*2]*minus[i*2+1]

if minus_num%2!=0 and minus:
    minus_sum+=minus[-1]

# print("plus:",plus)
# print("minus:",minus)
# print("plus_sum:",plus_sum)
# print("minus_sum:",minus_sum)
# print("ones:",ones)
print(plus_sum+minus_sum+ones)
    