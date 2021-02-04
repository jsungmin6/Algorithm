'''
sort 조건을 잘 생각해야 한다.
numbers가 1000 이하니 *3을해서 비교한다.
'''
numbers=[0,0,0,0,0]
def solution(numbers):
    nums=[]
    for i in numbers:
        nums.append(str(i))
    nums.sort(key=lambda x:x*3,reverse=True)
    if nums[0]=="0" and nums[-1]=="0":
        return "0"
    answer = ''.join(nums)
    return answer

print(solution(numbers))