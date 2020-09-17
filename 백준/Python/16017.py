array=list()

array=[8,3,3,8]

if array[0]==8 and array[3] ==9 and array[1]==array[2]:
    print('ignore')
elif array[0]==9 and array[3] ==8 and array[1]==array[2]:
    print('ignore')
elif array[0]==8 and array[3] ==8 and array[1]==array[2]:
    print('ignore')
elif array[0]==9 and array[3] ==9 and array[1]==array[2]:
    print('ignore')
else:
    print('answer')
