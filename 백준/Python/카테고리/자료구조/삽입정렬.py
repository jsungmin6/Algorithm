
def insertion1(arr):
    l = len(arr)
    for e in range(1,l):
        for i in range(e-1,0,-1):
            if arr[i-1] > arr[i]:
                arr[i-1],arr[i] = arr[i],arr[i-1]
    return arr



def insertion2(arr):
    
    l = len(arr)
    for e in range(1,l):
        i = e
        while i > 0 and arr[i-1] > arr[i]:
            arr[i-1],arr[i] = arr[i],arr[i-1]
            i-=1
    return arr

print(insertion1([12,14,2,12412,4,12,41,4,4,1,413,4,4,21,4,54,35]))