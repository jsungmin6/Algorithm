from itertools import permutations
numbers="55"

def creat_p(numbers):
    li=set()
    for i in range(1,len(numbers)+1):
        for j in permutations(numbers,i):
            li.add(int(''.join(j)))
    return list(li)

def solution(numbers):
    answer=0
    p=creat_p(numbers)
    print("p:",p)
    max_p=max(p)
    primes=[]
    is_prime=[True]*(max_p+1)
    is_prime[0]=False
    is_prime[1]=False
    for i in range(2,max_p):
        if is_prime[i]:
            primes.append(i)
            for j in range(i*i,max_p+1,i):
                is_prime[j] = False
    
    for i in p:
        if is_prime[int(i)]:
            answer+=1
        
    return answer

print(solution(numbers))