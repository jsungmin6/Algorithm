'''
풀이
두번 이상 같은 move를 하지 않는다. 이것을 저장한다.
bfs로 최단경로를 찾아본 후 오름차순 출력한다.
'''
from collections import deque
from copy import deepcopy
import sys
sys.setrecursionlimit(200000)
code = {"a" : 0,"b" : 1,"c" : 2,"d" : 3,"e" : 4,"f" : 5,"g" : 6,"h" : 7,"i" : 8}

move = {}
move["a"] = [0,1,3,4]
move["b"] = [0,1,2]
move["c"] = [2,3,4,5]
move["d"] = [0,3,6]
move["e"] = [1,3,4,5,7]
move["f"] = [2,5,8] 
move["g"] = [3,4,6,7] 
move["h"] = [6,7,8]
move["i"] = [4,5,7,8]   

mat = []
visited = set()

def change_mat(mat,s):
    change_list = move[s]
    new = deepcopy(mat)

    for i in change_list:
        new[i] = (mat[i]+1)%4
    
    return new

for i in range(3):
    temp = list(map(int,input().split()))

    for j in temp:
        mat.append(j)

def clock_to_str(clock):
    return ''.join(map(str,clock))


def back(clock,visited,prev):
    str_clock = clock_to_str(clock)
    if str_clock in visited:
        return
    visited.add(str_clock)

    for s in code.keys():
        idx = code[s]

        new_mat = change_mat(clock,s)
        str_new_mat = clock_to_str(new_mat)
        
        if str_new_mat in visited:
            return

        new_prev = prev+[idx]

        if sum(new_mat) == 0:
            print("new_prev : ",new_prev)
            exit()

        back(new_mat,visited,new_prev)
    
    print("끝?")

back(mat,visited,[])

        
    

    



