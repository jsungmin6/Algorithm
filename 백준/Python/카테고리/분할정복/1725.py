# 히스토그램

'''
오른쪽 지역 왼쪽지역, 경계를 포함하는 지역을 구분하여 가장 큰 것을 리턴하는 방식으로 분할정복한다.
'''
from sys import stdin

input = stdin.readline

N = int(input())
histograms = [int(input()) for i in range(N)]


def histogram(s, e):
    if s == e:
        return histograms[s]
    mid = (s+e)//2
    left = mid
    right = mid+1
    ret = max(histogram(s, left), histogram(right, e))

    # 경계를 포함하는 지역
    # 시작이 s 이고 끝지점이 e 인부분에서 mid는 구해놓은 상황
    # 그러면 s<=mid<=e 인 영역에서 최대 영역을 리턴해야 함.
    # 크기가 1(s==e)인 구간은 위에서 return 했으니 최소 2다.
    # 먼저 mid,mid+1 중에 h가 작은 막대의 크기를 구하고 x 2한다. 이게 첫 후보다.
    # left right를 확장해나가면서 max크기를 비교하고 s==left right==e 가 되면 가장 큰 후보가 남음
    # 그 후보와 위에서 구한 ret 값과 비교해 max 값을 리턴한다.

    w = 2
    h = min(histograms[left], histograms[right])
    max_candidate = w*h
    while s < left or right < e:
        if right < e and (left == s or histograms[left-1] < histograms[right + 1]):
            right += 1
            w += 1
            h = min(h, histograms[right])
        else:
            left -= 1
            w += 1
            h = min(h, histograms[left])
        max_candidate = max(max_candidate, w*h)

    return max(max_candidate, ret)


print(histogram(0, N-1))
