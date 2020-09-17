countScore = 0

def downBox(n):
    for i in range(5,0,-1):
        for j in range(4):
            if n[i][j]==0:
                n[i][j]=n[i-1][j]
                n[i-1][j]=0
    checkBox(n)



def checkBox(n):
    pointLine=[]
    for i in range(len(n)):
        if n[i] == [1,1,1,1]:
            pointLine.append(i)
            global countScore
            countScore+=1

    if pointLine:
        for i in pointLine:
            n[i] = "2"
        n.remove("2")
        for _ in range(len(pointLine)):
            n.insert(0,[0,0,0,0])
        pointLine=[]
        downBox(n)

    if 1 in n[0]:
        del n[-1]
        del n[-1]
        n.insert(0,[0,0,0,0])
        n.insert(0,[0,0,0,0])
    if 1 in n[1]:
        del n[-1]
        n.insert(0,[0,0,0,0])


def printBox(n):
    for i in n:
        print(i)
    print()

def countBox(n):
    count=0
    for i in n[2:7]:
        for j in i:
            if j==1:
                count+=1
    return count


D=18
# data=["1 1 1","2 3 0","3 2 2","3 2 3","3 1 3","2 0 0","3 2 0","3 1 2"]

data=["1 2 2","1 2 3","2 0 0","1 2 0","1 1 2","1 1 0","2 3 0","3 0 1","3 1 3","2 1 0"
,"1 2 0","2 3 0","2 2 1","1 2 2","3 0 3","1 2 0","2 2 0","3 2 3"]
array = list()
box = [[0,0,0,0] for _ in range(6)]
box2 = [[0,0,0,0] for _ in range(6)]
for k in range(D):
    t,x,y=map(int,data[k].split());
    # index = y;
    # #세로축
    # if t==1:
    #     for i in range(len(box)):
    #         if box[i][index] != 0:
    #             box[i-1][index]=1
    #             break
    #         elif i==5:
    #             box[i][index]=1
    #
    # if t==2:
    #     for i in range(len(box)):
    #         if box[i][index] != 0 or box[i][index+1] != 0:
    #             box[i-1][index]=1
    #             box[i-1][index+1]=1
    #             break
    #         elif i==5:
    #             box[i][index]=1
    #             box[i][index+1]=1
    #
    # if t==3:
    #     for i in range(len(box)):
    #         if box[i][index] != 0:
    #             box[i-1][index]=1
    #             box[i-2][index]=1
    #             break
    #         elif i==5:
    #             box[i][index]=1
    #             box[i-1][index]=1
    #
    # checkBox(box)


    #가로축


    index = x;
    if t==1:
        for i in range(len(box2)):
            print("i :", i)
            print(box2[i][index])
            if box2[i][index] != 0:
                box2[i-1][index]=1
                break
            elif i==5:
                box2[i][index]=1

    if t==2:
        for i in range(len(box2)):
            print("i :", i)
            print(box2[i][index])
            if box2[i][index] != 0:
                box2[i-1][index]=1
                box2[i-2][index]=1
                break
            elif i==5:
                box2[i][index]=1
                box2[i-1][index]=1

    if t==3:
        for i in range(len(box2)):
            if box2[i][index] != 0 or box2[i][index+1] != 0:
                box2[i-1][index]=1
                box2[i-1][index+1]=1
                break
            elif i==5:
                box2[i][index]=1
                box2[i][index+1]=1

    printBox(box2)

    checkBox(box2)

print("box1")
printBox(box)
print("box2")
printBox(box2)

count1 = countBox(box)
count2 = countBox(box2)
print("countScore : ", countScore)
print("countBoxNum : ", count1+count2)
