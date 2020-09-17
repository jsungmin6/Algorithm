data='99'
centerIndex=len(data)//2
ninecheck=True

for i in range(len(data)):
    if data[i] != '9':
        ninecheck=False

if ninecheck:
    print(int(data)+2)
else:
    if len(data)%2==1:
        left=data[0:centerIndex]
        right=left[::-1]

        if int(left+str(int(data[centerIndex]))+right) > int(data):
            print(left+str(int(data[centerIndex]))+right)
        elif data[centerIndex]=='9':
            left=str(int(left)+1)
            right=left[::-1]
            print(left+'0'+right)
        else:
            print(left+str(int(data[centerIndex])+1)+right)
    else:
        centerIndex=centerIndex-1
        left=data[0:centerIndex]
        right=left[::-1]

        if int(left+str(int(data[centerIndex]))+str(int(data[centerIndex]))+right) > int(data):
            print(left+str(int(data[centerIndex]))+str(int(data[centerIndex]))+right)
        elif data[centerIndex]=='9':
            left=str(int(left)+1)
            right=left[::-1]
            print(left+'00'+right)
        else:
            print(left+str(int(data[centerIndex])+1)+str(int(data[centerIndex])+1)+right)
