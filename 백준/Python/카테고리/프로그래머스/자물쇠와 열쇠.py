'''
풀이
lock의 구멍수 != key의 돌출부 수 False
lock의 구멍 사이 최대 길이 > key 돌출부 최대 길이 
lock 의 구멍 좌표 찾아놓기
key 후보들 4바퀴씩 돌리면서 lock 구멍좌표와 일치하는지 확인
key 후보들 중복제거 위해 비트마스킹 or set 사용
set을 사용하니 배열을 1차원으로 바꿈 =>[[1, 1, 1], [1, 1, 0], [1, 0, 1]] 111110101
'''
