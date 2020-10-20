#캐시

#풀이 방법

'''
자료구조 문제
큐 구현
데크(deque사용)
'''

# # # # # # # # # # # # # # # # # # # # #
def solution(cacheSize,cities):
    elapsed = 0
    cache = collections.deque(maxlen=cacheSize)

    for c in cities:
        c = c.lower()
        #캐시 히트 시 재삽입 처리
        if c in cache:
            cache.remove(c)
            cache.append(c)
            elapsed+=1
        else: #캐시 미스 시 삽입만
            cache.append(c)
            elapsed+=5
    return elapsed
