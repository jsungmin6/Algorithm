'''
모든 경우를 탐색
'''
import deque

def bfs(numbers,target):
    

def solution(numbers, target):
    if numbers==[] and target==0:
        return 1
    elif numbers==[]:
        return 0
    else:
        return solution(numbers[1:],target-numbers[0])+solution(numbers[1:],target+numbers[0])

##BFS
import collections

def solution(numbers, target):
    answer = 0
    stack = collections.deque([(0, 0)])
    while stack:
        current_sum, num_idx = stack.popleft()

        if num_idx == len(numbers):
            if current_sum == target:
                answer += 1
        else:
            number = numbers[num_idx]
            stack.append((current_sum+number, num_idx + 1))
            stack.append((current_sum-number, num_idx + 1))

    return answer
