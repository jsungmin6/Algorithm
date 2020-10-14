#2D 행렬 검색

#풀이 방법

'''
이진검색 문제 같지만 이진검색으로는 풀이가 어려움
예상과 달리 다른 방법으로 풀리는 경우가 있으므로, 실제고딩 테스트 시에도 예상 방법대로 안풀리면
너무 시간을 낭비하지 말자

'''

# # # # # # # # # # # # # # # # # # # # # 투포인터
class Solution:
    def searchMatrix(self, matrix, target):
        return any(target in row for row in matrix)
