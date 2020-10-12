#원점에 K번째로 가까운 점

#풀이 방법

'''
힙 사용
'''

# # # # # # # # # # # # # # # # # # # # #

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap=[]
        for (x,y) in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(heap,(dist,x,y))

        result=[]
        for _ in range(K):
            (dist,x,y) = heapq.heappop(heap)
            result.append((x,y))
        return result
