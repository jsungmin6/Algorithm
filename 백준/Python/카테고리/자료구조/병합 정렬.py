def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left,right)

def merge(left,right):
    result = []
    left_point, right_point = 0,0

    #서로 비교할 데이터가 있다는 뜻
    while left_point < len(left) and right_point < len(right):
        if left[left_point] > right[right_point]:
            result.append(right[right_point])
            right_point+=1
        else:
            result.append(left[left_point])
            left_point+=1
    
    #왼쪽이 남았다
    while left_point < len(left):
        result.append(left[left_point])
        left_point+=1

    #오른쪽이 남았다.
    while right_point < len(right):
        result.append(right[right_point])
        right_point+=1
    
    return result

arr=[12,23,3,21,4,2,2,3,44,5,6]

print(merge_sort(arr))