def check(candidate,cul):
    current_row=len(candidate)
    for queenrow in range(current_row):
        if candidate[queenrow]==cul or abs(candidate[queenrow]-cul) == current_row - queenrow:
            return False
    return True

def DFS(N,current_row,candidate):
    global result
    if current_row == N:
        result+=1
        return

    for cul in range(N):
        if check(candidate,cul):
            candidate.append(cul)
            DFS(N,current_row+1,candidate)
            candidate.pop()


result=0
DFS(4,0,[])
print(result)
