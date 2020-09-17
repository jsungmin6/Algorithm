import math
n=64
a,b=str(math.sqrt(n)*4).split('.')
if(len(b)>8):
    print(format(math.sqrt(n)*4,'.8f'))
else:
    print(math.sqrt(n)*4)
