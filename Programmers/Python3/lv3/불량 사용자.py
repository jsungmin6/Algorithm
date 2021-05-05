'''
풀이

백트래킹을 이용해 보든 경우를 탐색한다.

형식에 맞는 아이디를 포문을 돌며 dfs로 탐색한다.
이미 제재처리한 id, 형식에 맞지 않는 id는 제외한다.

총 종류의 가지 수를 센다.
즉 조합의 수다.
'''

def change_v_to_bit(v):
    bit = ""
    for i in range(len(v)):
        bit += str(v[i])
    return bit

def is_in(bit):
    global result
    if bit in result:
        return True
    return False

def match(ban,user):
    if len(ban) != len(user):
        return False
    for i in range(len(ban)):
        if ban[i] == "*":
            continue
        else:
            if ban[i] != user[i]:
                return False
    return True

def dfs(user_id, banned_id,n,v):
    global result
    answer = 0
    if n == len(banned_id):
        bit = change_v_to_bit(v)
        if not is_in(bit):
            result.add(bit)
            return 1
        return 0
    
    target = banned_id[n]
    for i in range(len(user_id)):
        if v[i]:
            continue
        if match(target,user_id[i]):
            v[i] = 1
            answer += dfs(user_id,banned_id,n+1,v)
            v[i] = 0 
    
    return answer


result = set()

def solution(user_id, banned_id):
    global result

    visited = [0]*len(user_id)

    cnt = dfs(user_id, banned_id,0,visited)

    return cnt

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
print(solution(user_id, banned_id))

