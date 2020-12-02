# 증가한는 녀석이 있니? 체크
# 그러면 제일 뒷자리 제거

N, K = map(int, input().split())
S = list(input())


def ch(S):  # 몇번째 인덱스를 제거해야 하는지
    for i in range(0, len(S)-1):
        if S[i] < S[i+1]:
            return i
    return len(S)-1


answer = []
for _ in range(K):
    i = ch(S)
    del S[i]

print(''.join(S))
