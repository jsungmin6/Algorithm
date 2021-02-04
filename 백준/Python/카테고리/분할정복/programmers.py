arr=[[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]

one=0
zero=0
def check_one(arr):
    if len(set(sum(arr,[]))) == 1:
        print('True')
        return True
    print('False')
    return False

def press(N,arr):
    global one
    global zero
    for i in arr:
        print(i)
    if N==1:
        if arr[0][0] == 1:
            one+=1
            return
        else:
            zero+=1
            return
    if check_one(arr):
        if arr[0][0] == 1:
            one+=1
            return
        else:
            zero+=1
            return
    
    N = N//2
    for i in range(2):
        for j in range(2):
            ret_map = []
            for k in range(N):
                ret_map.append(arr[i*N+k][j*N:j*N+N])
            
            press(N, ret_map)
    
    
            

def solution(arr):
    press(len(arr),arr)
    return [zero,one]

print(solution(arr))