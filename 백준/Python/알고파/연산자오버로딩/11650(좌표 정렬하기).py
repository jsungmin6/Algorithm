class Coord:
    __x__=0
    __y__=0
    def __init__(self, first, second):
        self.x = first
        self.y = second
    
    def __lt__(self, other):
        if self.x != other.x:
            return self.x < other.x

        return self.y < other.y;

N=int(input())
dots=[]
for _ in range(N):
    dots.append(Coord(*list(map(int,input().split()))))

dots.sort()

for i in dots:
    print(i.x,i.y)