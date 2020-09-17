#배열을 만든후 각 요소에 몇개의 줄이 걸렸는지 체크



# array=[0 for i in range(N+1)]
#
# array=[0 for i in range(N+1)]
# #1-2 2-4 3-6.... 짝수를 먼저 체크한다.
# for i in range(N+1):
#     s=i;
#     e=i*2
#     for j in range(s,e,1):
#         array[j]+=1
#         if j == N:
#             break
#
#
# array=[0 for i in range(N+1)]
# #1-4, 3-10... 홀수를 체크한다.
# for i in range(1,N+1,2):
#     s=i;
#     e=i*3+1
#     for j in range(s,e,1):
#         array[j]+=1
#         if j==N:
#             break
# print(array)



#규칙 파악 후 답체크

K=int(input())

data=[]

for _ in range(K):

    N= int(input())

    #짝수 규칙 1,1,2,2,3,3,4,4...
    if N%2==1:
        A=N//2+1
    else:
        A=N//2

    #홀수 규칙 1 1 2 / 1 2 2 / 3 3 4  /3 4 4 / ...
    T=N%3
    S=N//3
    if T==0:
        if S%2==1:
            B=S+1
        else:
            B=S
    elif T==1:
        if S%2==1:
            B=S
        else:
            B=S+1
    elif T==2:
        B=S+1;

    data.append(A+B)

for i in data:
    print(i)
