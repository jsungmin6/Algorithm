#다트 게임

#풀이 방법

'''
문자열 처리 문제
0을 중간에 끼워 10을 구분할 수 있도록 함.
'''

# # # # # # # # # # # # # # # # # # # # #
def solution(dartResult):
    nums= [0]
    for s in dartResult:
        if s == 'S':
            nums[-1] **=1
            nums.append(0)
            print(nums)
        elif s == 'D':
            nums[-1] **=2
            nums.append(0)
            print(nums)
        elif s == 'T':
            nums[-1] **=3
            nums.append(0)
            print(nums)
        elif s == '*':
            # 이전 값, 그 이전 값 모두 두 배 처리
            nums[-2] *= 2
            print(nums)
            if len(nums) > 2:
                nums[-3] *= 2
                print(nums)
        elif s == '#':
            nums[-2] *=-1
            print(nums)
        else:
            # 자릿수 올림
            nums[-1] = nums[-1]*10 +int(s)
            print(nums)
    return sum(nums)

print(solution('1S1D*3T'))
