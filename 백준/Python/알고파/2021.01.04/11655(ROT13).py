S = list(input())

for i in S:
    if i.isalpha():
        if i.isupper():
            if ord(i)+13 >90:
                print(chr(ord(i)+13-26),end='')
            else:
                print(chr(ord(i)+13),end='')
        else:
            if ord(i)+13 > 122:
                print(chr(ord(i)+13-26),end='')
            else:
                print(chr(ord(i)+13),end='')
    else:
        print(i,end='')