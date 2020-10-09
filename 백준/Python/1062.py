#가르침 G4

#풀이방법

#사용된 알파벳을 비트마스킹으로 변환후 단어배열에 저장 abc->[1,1,1,0,0,0,0,0,....]
#단어배열 [[1,1,1],[0,1,0]...] 이럴꺼임
#단어배열을 조합으로 만듬. iCy
#가장 많은 수의 조합부터 1개씩 이면서 비트마스킹 and연산 후 K를 넘는지 검사. K를 넘으면 제외
#그 중에 가장 큰 수를 저장하고 종료

################################################

from itertools import combinations

N,K = map(int,input().split())
data=['0']*27
bitdata=[]
for _ in range(N):
    for i in input():
        if data[ord(i)-97]=='0':
            data[ord(i)-97]='1'
    if data.count('1')<=K:
        bitdata.append(''.join(data))
    data=['0']*27


# print(bitdata)
answer=0
for count in range(len(bitdata),0,-1):
    # print(count)
    for combination in combinations(bitdata,count):
        # print(combination)
        union = 0
        for n in combination:
            # print(union)
            n=int(n,2)
            union |= n
        # print(bin(union))
        strs = bin(union).count('1')
        # print('strs',strs)
        if K >= strs:
            answer=max(answer,count)
    if answer!=0:
        break

print(answer)


#다른풀이

from sys import stdin, exit


def dfs(idx, cnt):
    global answer

    if cnt == k - 5:
        read_cnt = 0
        for word in words:
            for w in word:
                if not learn[ord(w) - ord('a')]:
                    break
            else:
                read_cnt += 1
        answer = max(answer, read_cnt) if answer else read_cnt
        return

    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt + 1)
            learn[i] = False


if __name__ == '__main__':
    answer = None
    n, k = map(int, stdin.readline().split())

    if k < 5 or k == 26:
        print(0 if k < 5 else n)
        exit(0)

    words = [set(stdin.readline().rstrip()) for _ in range(n)]
    learn = [False] * 26

    for c in ('a', 'c', 'i', 'n', 't'):
        learn[ord(c) - ord('a')] = True

    dfs(0, 0)
    print(answer)
