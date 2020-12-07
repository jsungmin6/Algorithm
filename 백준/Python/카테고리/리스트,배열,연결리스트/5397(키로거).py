'''
"만약 커서의 위치가 줄의 마지막이 아니라면, 커서 및 커서 오른쪽에 있는 모든 문자는 오른쪽으로 한 칸 이동한다."
이게 무슨말인지 몰라서 한참 봤다...
즉 글자가 중간에 하나 들어오면 뒤에있는 글자는 하나씩 밀린다는 뜻.

이것또한 두개의 스택을 이용해서 풀면 최소 시간복잡도로 해결 가능 할 듯.
'''
import sys
input = sys.stdin.readline

t = int(input())


for _ in range(t):
    pwd = input().rstrip()
    left = []
    right = []
    for i in pwd:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)
    print(''.join(left + right[::-1]))


