def quick(arr):
    if len(arr) < 2:
        return arr
    
    pivot = arr[0]
    left=[]
    right=[]
    for i in range(1,len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    
    return quick(left) + [pivot] + quick(right)

arr = [12,12,3123123,313123,12312,312312,34,35455,6476,567,4]

print(quick(arr))