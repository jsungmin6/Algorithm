hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_f(key):
    return key % 5

def save_data(data,value):
    hash_address = hash_f(get_key(data))
    hash_table[hash_address] = value

def read_data(data):
    hash_address = hash_f(get_key(data))
    return hash_table[hash_address]

def csave_data(data,value):
    index_key = get_key(data)
    hash_address = hash_f(index_key)
    #값이 없으면 [키,value] 로 넣어준다.
    if hash_table[hash_address] == 0:
        hash_table[hash_address] = [[index_key,value]]
    #값이 있을경우
    else:
        #완전히 일치하는 키가 있을경우 대체
        for i in range(len(hash_table[hash_address])):
            if hash_table[hash_address][i][0] == index_key:
                hash_table[hash_address][i][1] = value
                return
        #완전히 일치하는게 아니라 해쉬함수결과만 같은것일경우 체이닝
        hash_table[hash_address].append([index_key,value])
        

def lsave_data(data, value):
    index_key = get_key(data)
    hash_address = hash_f(index_key)
    
    if hash_table[hash_address] != 0:
        for i in range(hash_address, len(hash_table)):
            if hash_table[i] == 0:
                hash_table[i] = [index_key, value]
                return
            elif hash_table[i][0] == index_key:
                hash_table[i][1] = value
                return
            
    else:
        hash_table[hash_address] = [index_key, value]

