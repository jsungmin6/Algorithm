def selection(arr):

    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    return arr