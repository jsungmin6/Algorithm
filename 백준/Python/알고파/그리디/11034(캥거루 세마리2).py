# 오름차순이라 할때 ABC 가 주어지면 answer = max(B-A,C-B)-1이다. 

while True:
    try:
        A,B,C = map(int,input().split())
        answer = max(B-A,C-B)-1
        print(answer)
    except:
        break