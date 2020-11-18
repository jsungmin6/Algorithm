# 부분배열 고르기

'''
히스토그램과 유사한 문제
왼쪽영역과 오른쪽 영역 그리고 경계를 포함한 중간지역을 계산해 그 중 가장 큰 영역을 리턴하는 식으로 해야한다.
중간지역은 while문을 사용해 탐욕법적인 방법으로 구한다.
'''


def solve(s, e):
    if s == e: #범위가 1일때 자기자신 리턴 
        return A[s] * A[s]
    mid = (s+e)//2
    #왼쪽구역과 오른쪽 구역중 큰 값을 ret 에 담는다.
    ret = max(solve(s, mid), solve(mid+1, e))

    #중간지역 가장 최소단위를 ret 과 비교해 담는다.
    left = mid
    right = mid + 1
    _sum = A[left] + A[right]
    min_val = min(A[left], A[right])
    ret = max(ret, min_val * _sum)
    #중간지역을 확장한 후 ret와 비교해 담아준다.
    while left > s or right < e:
        if right < e and (left == s or A[left-1] < A[right + 1]):
            right += 1
            _sum += A[right]
            min_val = min(min_val, A[right])
        else:
            left -= 1
            _sum += A[left]
            min_val = min(min_val, A[left])
        ret = max(ret, min_val * _sum)
    return ret

input()
A = list(map(int, input().split()))
print(solve(0, len(A)-1))






