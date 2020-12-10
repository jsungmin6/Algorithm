'''
stack 을 두개 사용하면 가능하지 않을까
태그 뽑아내기용 stack 과
뽑아낸 태그의 규칙성 파악하는 stack

1.<가 오면 stack을 비워주고 <부터 채워 줌.
2.만약 < 다음에 /가 오고 바로 다음이 > 이면 스택을 비워줌
2.< 이후 > 가오면 안에 스트링을 넘기는데 < 과 </를 구분해 string만 넘기도록 함 혹시 a 태그이면 a 만 넘김

'''

while True:
    stack=[]
    html=list(input())
    if not html:
        print('legal')
        continue
    if html[0] =='#':
        break
    parse_stack=[]
    for s in range(len(html)):
        # print('stack:',stack)
        # print('parse_stack:',parse_stack)
        # print('s:',s)
        if html[s]=='<':
            parse_stack=[]
        elif html[s]=='/' and html[s-1] =='<':
            parse_stack=[]
        elif html[s]=='/' and s != len(html)-1 and html[s+1]=='>':
            parse_stack=[]
        elif html[s]== '>':
            if parse_stack:
                temp = ''.join(parse_stack)
                if temp[0] == 'a':
                    temp = 'a'
                if not stack:
                    stack.append(temp)
                elif stack[-1] == temp:
                    stack.pop()
                else:
                    stack.append(temp)
        else:
            parse_stack.append(html[s])
    # print("last stack:",stack)
    if stack:
        print('illegal')
    else:
        print('legal')


#다른풀이 : 단어단위로 자르는게 훨씬 깔끔하다
from sys import stdin

while True:
    word = stdin.readline().rstrip()
    if word == "#": break

    stack = []
    word = word.replace(" />", "/>").replace("<", "|<").replace(">", ">|").split("|")

    for w in word:
        if w == "": continue

        elif w == " ":
            continue

        elif w[:2] == "</" and w[-1] == ">":
            if stack and stack[-1] == w[2:-1]: stack.pop()
            else: stack.append(w[1:])

        elif w[0] == "<" and w[-2:] == "/>":
            continue

        elif w[0] == "<" and w[-1] == ">":
            w = w.split()
            if len(w) > 1: stack.append(w[0][1:])
            else: stack.append(w[0][1:-1])

    p = "illegal" if stack else "legal"
    print(p)
