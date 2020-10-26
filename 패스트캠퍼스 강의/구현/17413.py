# 단어 뒤집기 2

# 풀이 방법

'''
단어가 들어올 경우 단어를 저장해 둘 리스트 하나 생성
-이후 ' ' or '<' 가 들어올경우 단어를 뒤집어서 출력
단어가 아닌경우 바로 출력
'<' 가 들어올 경우 '>'가 들어올 때까지 그대로 출력
'''
# # # # # # # # # # # # # # # # # # # # # 내 풀이
S = input()
S_len = len(S)
i = 0
word = []n
answer = []

while i < S_len:
    if S[i] == ' ':
        answer.append(''.join(word[::-1]))
        answer.append(S[i])
        word = []
        i += 1
    if S[i] == '<':
        if word:
            answer.append(''.join(word[::-1]))
            word = []
        while S[i] != '>':
            answer.append(S[i])
            i += 1
    if S[i] == '>':
        answer.append(S[i])
        i += 1
        continue
    word.append(S[i])
    i += 1
answer.append(''.join(word[::-1]))
print(''.join(answer))
