'''
풀자
포인터를 두고 왼쪽부터 탐색한다.

시작부분이 0이 나오면 바로 뒤에 1이 나와야 통과

시작부분이 1이 나오면 '100 ~~~ 111' 형식이니 0이 두번 이상 나오고 이후에 1이 최소 1개 나오고 마지막 1나올때까지 탐색하고 종료


'''
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    code = input().rstrip()
    l = len(code)
    i = 0
    ch = True

    while i < l :
        # 시작이 0인경우 바로 뒤에 1이 안오면 실패
        if code[i] == "0":
            #남은 수가 2개가 안될 때 실패(01이 최소 길이기 때문)
            if l-i < 2:
                ch=False
                break
            elif code[i+1] != "1":
                ch=False
                break
            else:
                i+=2
        # 시작이 1이 올경우
        else:
            #남은 수가 4개가 안될 때 실패(1001이 최소 길이기 때문)
            if l-i < 4:
                ch=False
                break
            # 다음 2개가 0이 아닐결우 실패
            elif code[i+1] != "0" or code[i+2] != "0":
                ch=False
                break
            else:
                i+=2 # 0,0 추가
                while code[i] != "1": # 1찾기
                    i+=1
                    #1을 못찾고 0으로 끝나면 실패
                    if i==l:
                        ch=False
                        break
                
                if not ch:
                    break

                # 현재 code[i] == 1 , 1까지 찾은 상태

                while code[i] != "0": # 0찾기
                    i+=1
                    if i==l:
                        break
                
                # 현재 code[i] == 0
                
                # 100패턴으로 이어질경우 i 위치를 다시 1로 맞춰준다.
                if i+1 < l and code[i-2] == "1" and code[i+1] == "0":
                    i-=1
                    
    if ch:
        print("YES")
    else:
        print("NO")
    
            
