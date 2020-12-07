S = list(input())
c = {"+": 1,"-" :1,"*" : 2, "/":2}
st = []
answer = []
for s in S:
    # print("stack: ",st)
    # print("answer: ",answer)
    if s == ")":
        while st[-1]!="(":
            answer.append(st.pop())
        st.pop()
    elif s == "(":
        st.append(s)
    elif s == "*" or s == "/" or s =="+" or s =="-":
        if not st or st[-1] == "(":
            st.append(s)
            continue
        if c[st[-1]] < c[s]:
            st.append(s)
            continue
        while c[st[-1]] >= c[s]:
            answer.append(st.pop())
            if not st:
                st.append(s)
                break
            if st[-1] == "(":
                st.append(s)
                break
            if c[st[-1]] < c[s]:
                st.append(s) 
                break
    else:
        answer.append(s)


if st:
    while st:
        answer.append(st.pop())

print(''.join(answer))
    
#다른 답안
a=""
s=[]
r={"+":2,"-":2,"*":3,"/":3,"(":0,")":1}
for i in input():
	if i in r: 
		while s and r[i]:
			if s[-1]=="(":
				if i==")":s.pop()
				break
			elif r[s[-1]]>=r[i]:a+=s.pop()
			else:break
		if i!=")":s+=i
	else: a+=i
print(a+"".join(reversed(s)))