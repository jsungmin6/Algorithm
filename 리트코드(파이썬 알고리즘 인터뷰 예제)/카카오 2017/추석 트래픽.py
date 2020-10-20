#추석 트래픽

#풀이 방법

'''
슬라이딩 윈도우
하루치 로그를 처음부터 끝까지 스캔하기에 범위가 큼
로그의 시간 단위가 밀리초. 1밀리초씩 증가하면서 슬라이딩 윈도우를 진행 할 수 없음
효율적인 접근 전략 필요
요청량이 변하는 순간은 로그의 시작과 끝 뿐임.
각 로그별 2번씩 비교 연산만 수행

'''

# # # # # # # # # # # # # # # # # # # # #
def solution(lines):
    #로그의 시작, 종료 시각 저장
    combined_logs = []
    for log in lines:
        logs = log.split(' ')
        timestamp = datetime.datetime.strptime(logs[0] + ' ' + logs[1],
                    "%Y-%m-%d %H:%M:%S.%f").timestamp()
        combined_logs.append((timestamp,-1))
        combined_logs.append((timestamp - float(logs[2][:-1]) + 0.001,1))

    accumulated=0
    max_requests=1
    combined_logs.sort(key=lambda x:x[0])
    for i,elem1 in enumerate(combined_logs):
        current = accumulated

        #1초 미만 윈도우 범위 요청 수 계산
        for elem2 in combined_logs[i:]:
            #다음 로그부터 시작타임이든 끝 타임이든 1초를 넘으면 종료
            if elem2[0] - elem1[0] > 0.999:
                break
            #1초를 넘지 않고, 시작로그이면 current에 +1
            if elem2[1] > 0:
                current += elem2[1]
        #최대값 current 를 max_requests에 저장
        max_requests = max(max_requests,current)
        #시작 로그가 시작지점 이었으면 1을 더해서 다음 for문 진행, 끝지점이었으면 -1 해주고 진행.
        accumulated +=elem1[1]

    return max_requests
