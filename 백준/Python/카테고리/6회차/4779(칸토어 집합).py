'''
풀이



'''

#N 은 나머지의 개수
def cantore(start,N,li):
    if N==0:
        return
    
    N //= 3
    s1 = start + 0*N
    s2 = start + 1*N
    s3 = start + 2*N

    for i in range(s1,s1+N):
        li[i] = "-"
    for i in range(s2,s2+N):
        li[i] = " "
    for i in range(s3,s3+N):
        li[i] = "-"
    
    cantore(s1,N,li)
    cantore(s3,N,li)
    
    return li

while True:
    try:
        N = int(input())
        if N == 0:
            print("-")
            continue
        arr = [0]*(3**N)
        li = cantore(0,3**N,arr)

        for i in li:
            print(i,end='')
        print()
    except:
        break
