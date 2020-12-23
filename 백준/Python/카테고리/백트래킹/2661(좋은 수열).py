'''
규칙을 생각해도 따로 없다.
모든 경우를 생각해야 한다.
다음 수가 결정되는 경우의 수는 3개
3개 모두 나쁜 수열이라면 back
결과가 N인것을 모으고 min값을 찾을려고 했으나 1부터 넣으면
조건을 충족하는 첫 번째 수가 그냥 최소이다.
'''

N = int(input())
temp = []


def check(temp):
    l = len(temp)
    for i in range(1, l//2+1):
        if temp[-i:] == temp[-i*2:-i]:
            return False
    return True


def back(i):
    global min_result
    # print(i, temp)
    if i == N:
        result = int(''.join(temp))
        print(result)
        exit()
        return

    for n in ['1', '2', '3']:
        temp.append(n)
        if not check(temp):
            temp.pop()
            continue
        back(i+1)
        temp.pop()


back(0)
