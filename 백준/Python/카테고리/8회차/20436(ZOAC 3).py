'''

알파뱃을 좌표로 매핑한다.

계산한다.

'''

l,r = {},{}
l["q"] = (0,0)
l["w"] = (0,1)
l["e"] = (0,2)
l["r"] = (0,3)
l["t"] = (0,4)

l["a"] = (1,0)
l["s"] = (1,1)
l["d"] = (1,2)
l["f"] = (1,3)
l["g"] = (1,4)

l["z"] = (2,0)
l["x"] = (2,1)
l["c"] = (2,2)
l["v"] = (2,3)

r["y"] = (0,5)
r["u"] = (0,6)
r["i"] = (0,7)
r["o"] = (0,8)
r["p"] = (0,9)

r["h"] = (1,5)
r["j"] = (1,6)
r["k"] = (1,7)
r["l"] = (1,8)

r["b"] = (2,4)
r["n"] = (2,5)
r["m"] = (2,6)

sl,sr = input().split(" ")

l_cur,r_cur = l[sl],r[sr]

cnt = 0

for i in input():
    # print("i :",i)
    if i in l:
        l_next = l.get(i)
        dist = abs(l_cur[0]-l_next[0]) + abs(l_cur[1]-l_next[1])
        cnt+=dist+1 #거리와 입력
        l_cur = l_next
    elif i in r:
        r_next = r.get(i)
        dist = abs(r_cur[0]-r_next[0]) + abs(r_cur[1]-r_next[1])
        cnt+=dist+1 #거리와 입력
        r_cur = r_next
    # print("cnt : ",cnt)
print(cnt)
