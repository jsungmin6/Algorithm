#캠핑 S5

#풀이 방법

#몫과 나머지 활용해서 풀 수 있을 듯 하다.

################################################################
i=1
while True:
    L,P,V = map(int,input().split())

    if L==0 and P==0 and V==0:
        break

    A=V//P;
    B=V%P;

    if L<B:
        answer=A*L+L;
    else:
        answer=A*L+B;

    print('Case',i,end='')
    print(':',answer)
    i+=1
