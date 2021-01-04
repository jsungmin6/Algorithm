class Coord:
    __x__ = 0
    __y__ = 0
    def __init__(self, first, second):
        self.x = first
        self.y = second

    def __lt__(self, other):
        if self.y != other.y:
            return self.y < other.y

        return self.x < other.x

N = int(input())
xy = []
for i in range(N):
    tmp = tuple(map(int, input().split()))
    xy.append(Coord(tmp[0], tmp[1]))

xy.sort()

for c in xy:
    print(c.x, c.y)