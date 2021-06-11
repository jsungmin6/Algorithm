
def bubble1(arr):
    l = len(arr)
    for i in range(l-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

# 개선1
# 한 번도 안 바뀌었다면 버블소트 종료

def bubble2(arr):
    l = len(arr)
    for i in range(l-1,0,-1):
        swap = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swap=True
        if not swap:
            break
    return arr

#개선2
#마지막으로 swap한 곳까지만 버블소트 진행

def bubble3(arr):
    l = len(arr)
    last= l-1

    while last > 0:
        swap = 0
        for i in range(last):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                swap = i
        last = swap
    return arr

arr = [1,23,4,1,35,4,5,6,57,57,3624,5112,34,5,436,346,465,25,2456,245,435]

print(bubble3(arr))