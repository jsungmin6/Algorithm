'''
풀이 (시간초과)

심사관이 일이 끝나는 시간 리스트를 만든다.
각 심사관의 시간만큼 더한 후 가장 일이 일찍 끝나는 심사관을 찾는다.
그 심사관에게 일을 맡긴다.
해당 심사관의 일이 끝나는 시간을 늘려준다.

이분탐색 풀이

시간이 넉넉하다면 몇명을 처리할 수 있는가?

예를들어 심사관이 [7,10] 의 능률로 처리하고 40초가 주어진다 몇명을 처리할 수 있을까?

7의 능률을 가진사람은 5명, 10의 능률을 가진사람은 4명이다.

총 9명을 처리할 수 있다.

근데 지금 입국심사를 기다리는 사람 n = 6명이다. 그렇다면 40을 반으로 줄여본다.

20분으로 처리할 수 있는 사람은 각각 2명, 2명 해서 총 4명이다.

너무 적으니 다시 늘린다.

... (반복)

이런식으로 문제를 푸는게 이분탐색이다.

답 후보들이 전체 범위에서 1/2 씩 없어지기 때문에 lon(n)의 시간 복잡도로 풀 수 있다.

'''

def solve(mid,times):
    result = 0
    for time in times:
        result += mid//time
    return result

def solution(n, times):

    lo = 1
    hi = min(times)*n
    answer = 0

    while lo <= hi:
        mid = (lo+hi)//2

        result = solve(mid,times)

        if result < n: #너무 적게 사람을 처리한다 시간을 더 준다.
            lo = mid+1
        else: # 너무 많은 사람을 처리한다. 시간을 덜 준다.
            answer = mid
            hi = mid-1

    return answer


print(solution(6,[7,10]))