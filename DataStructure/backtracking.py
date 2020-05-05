def DFS(N,current_row,current_candidate,final):
    if N==current_row:
        final.append(current_candidate[:])
        return

    for candidate_col in range(N):
        if is_available(current_candidate,candidate_col):
            current_candidate.append(candidate_col)
            DFS(N,current_row+1,current_candidate,final)
            current_candidate.pop()

def is_available(current_candidate,candidate_col):
    current_row=len(current_candidate)
    for queen_row in range(current_row):
        if current_candidate[queen_row]==candidate_col or abs(current_candidate[queen_row]-candidate_col)==abs(queen_row-current_row):
            return False
    return True

def Nqueen(N):
    final=[]
    DFS(N, 0, [], final)
    return final
