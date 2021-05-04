'''
풀이
깊이를 i 라고 봤을 때 i-1 번째 깊이엣 ㅓ어떤 숫자를 선택했느냐에 따라 결과값이 달라진다.
즉 dp 문제이다.

깊이를 i, i번째 배열에서의 인덱스를 j라고 해보자

i번째깊이의 j번째 수의 합의 최대값은 무엇일까?
답은 i-1번째 깊이의 j-1번째수까지의 최대값과 j번째수까지의 최대값중 큰 값 + i번째깊이의 j번째 수일 것이다.

dp[i][j] = i번째 깊이의 j번째 인덱스가 가지는 합의 최댓값이다.

즉

dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]

'''
triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

def solution(triangle):
    dp = [[0 for i in range(502)] for j in range(502)]
    for i,tri in enumerate(triangle,start = 1):
        for j,t in enumerate(tri,start = 1):
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + triangle[i-1][j-1]

    answer = max(dp[len(triangle)])

    return answer


def solution2(triangle):
    dp = [[-1 for i in range(10)] for j in range(10)]

    def topdown(i,j):
        if i == len(triangle)-1 :
            return triangle[i][j]
        if dp[i][j] != -1:
            return dp[i][j]
        dp[i][j] = max(topdown(i+1,j+1),topdown(i+1,j)) + triangle[i][j]
        return dp[i][j]
    
    

    answer = topdown(0,0)

    for i in dp:
        print(i)
    return answer

print(solution2(triangle))

