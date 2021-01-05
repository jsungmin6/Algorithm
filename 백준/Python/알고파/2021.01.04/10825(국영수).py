'''
1.파이썬의 sort를 이용한 풀이
2.연산자 오버로딩을 이용한 풀이.
'''

class Coord:
    __name__ = 0
    __k__ = 0
    __e__ = 0
    __m__ = 0

    def __init__(self, name,k,e,m):
        self.name = name
        self.k = k
        self.e = e
        self.m = m

    def __lt__(self, other):
        if self.k != other.k:
            return self.k > other.k
        elif self.e != other.e:
            return self.e < other.e
        elif self.m != other.m:
            return self.m > other.m
        else:
            return self.name < other.name


import sys
input=sys.stdin.readline
N=int(input())
students=[]

for _ in range(N):
    name,k,e,m = input().rstrip().split()
    students.append(Coord(name,int(k),int(e),int(m)))

students.sort()

for i in students:
    print(i.name)

# ################sort 풀이
# import sys
# input=sys.stdin.readline
# N=int(input())
# students=[]

# for _ in range(N):
#     name,k,e,m = input().rstrip().split()
#     students.append([name,int(k),int(e),int(m)])

# # print(students)

# result = sorted(students,key=lambda x:(-x[1],x[2],-x[3],x[0]))

# for i in result:
#     print(i[0])