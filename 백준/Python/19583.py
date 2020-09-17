Time= "06:00 12:00 18:00"
data= ["06:00 shinyo17",
"06:00 kimchist",
"06:00 swoon",
"06:00 kheee512",
"06:00 Green55",
"09:00 kimchist",
"11:59 shinyo17",
"12:00 kimchist",
"17:59 swoon",
"17:59 swoon",
"18:00 kheee512",
"18:01 swoon",
"18:01 Green55",
"18:01 kheee512",
"18:01 swoon",
"18:21 jinius36",
"18:40 jeongyun1206"
]


S,E,Q = Time.split(' ')
array=set()

answer=0
i=0
while True:
    try:
        T,N = data[i].split()

        if T<=S:
            array.add(N)
            print(array)

        if T<=Q and T>=E:
            if N in array:
                answer+=1
                array.remove(N)
                print(array)
        i=i+1
    except:
        break

print(answer)
