'''
정렬 후 citations[i] >= i 인 i의 최대값을 구하면 될듯
'''
citations=[9,9,9,9,3]
def solution(citations):
    citations.sort(reverse=True)
    answer=1
    while True:
        if citations[answer-1] >= answer:
            answer+=1
            if answer>len(citations):
                answer-=1
                break
        else:
            answer-=1
            break
    return answer
print(solution(citations))