'''
'''

def add(n,m,t):
    if m==n:
        return t+n
    return add(n+1,m,t+n)



def st(arr,k):
    ak = arr[k]
    del arr[k]
    temp = sorted(arr)
    return [ak] + temp

arr = [2,5,6,1,3]
k=2
print(st(arr,k))
