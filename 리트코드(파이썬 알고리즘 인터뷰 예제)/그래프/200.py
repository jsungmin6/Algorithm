#섬의 개수

'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''

#풀이 방법

'''
[0][0]부터 끝까지 행렬을 돌면서 1을 만나면 dfs 실행 1주변 모든 1을 0으로 만들고 다시 dfs 이어감.
dfs 실행될 때마다 count+=1 해준다.
'''

# # # # # # # # # # # # # # # # # # # # # 내 풀이

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

dx=[1,0,0,-1]
dy=[0,1,-1,0]

x=len(grid[0])
y=len(grid)

def dfs(j,i):
    grid[j][i]='0'
    for k in range(4):
        newY=j+dy[k]
        newX=i+dx[k]
        if 0>newY or newY>=y or newX<0 or newX>=x:
            continue
        if grid[newY][newX]=='1':
            dfs(newY,newX)

count=0
for i in range(x):
    for j in range(y):
        if grid[j][i] == '1':
            dfs(j,i)
            count+=1
print(count)
