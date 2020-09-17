

array1=set(range(7,11))

array2=set(range(4,6))
print(array1)
print(array2)

if len(array1|array2) < len(array1)+len(array2):
    print(len(array1|array2)-1)
else:
    print(len(array1|array2)-2)
