import re


new_id=""
def solution(new_id):
    #1 소문자로
    new_id=new_id.lower()
    print(new_id)
    #2 나머지 문자 제거
    for char in '~!@#$%^&*()=+[{]}:?,<>/':
        new_id = new_id.replace(char,'')
    print(new_id)
    #3 .. -> .
    while '..' in new_id:
        new_id= new_id.replace("..",".")
    print(new_id)
    #4 양쪽 . 제거
    if new_id=='.' or new_id=='':
        new_id=''
    else:
        if new_id[0] == '.':
            new_id=new_id[1:len(new_id)]
        if new_id[-1] == '.':
            new_id=new_id[0:len(new_id)-1]
    print(new_id)
    #5 빈 문자열
    if new_id=='':
        new_id='a'
    print(new_id)
    #6
    if len(new_id)>=16:
        new_id=new_id[0:15]
    if new_id[-1] == '.':
        new_id=new_id[0:len(new_id)-1]
    print(new_id)
    #7
    if len(new_id)<=2:
        while len(new_id)<3:
            addstr=new_id[-1]
            new_id=new_id+addstr
    print(new_id)
solution(new_id)
#테스트 케이스 하나 안 맞음....
