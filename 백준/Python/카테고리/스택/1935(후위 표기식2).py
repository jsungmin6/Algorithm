'''
스택을 만들어 왼쪽부터 돌면서 문자는 스택에 넣고 연산자가 나오면 위에 두 문자를 꺼내어 계산하고 다시 스택에 넣음
'''

N=int(input())
S=list(input())
d={}
for i in range(N):
    d[chr(65+i)] = int(input())

st =[]

for i in range(len(S)):
    if S[i]=="*":
        A=st.pop()
        B=st.pop()
        C=B*A
        st.append(C)
    elif S[i]=="/":
        A=st.pop()
        B=st.pop()
        C=B/A
        st.append(C)
    elif S[i]=="+":
        A=st.pop()
        B=st.pop()
        C=B+A
        st.append(C)
    elif S[i]=="-":
        A=st.pop()
        B=st.pop()
        C=B-A
        st.append(C)
    else:
        j=d[S[i]]
        st.append(j)
    if i == len(S)-1:
        print(f"{st[0]:.2f}")

