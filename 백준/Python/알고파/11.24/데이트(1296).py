#데이트
'''
문자열, 구현
'''
import collections

OMINSIK = input()
L_c = OMINSIK.count('L')
O_c = OMINSIK.count('O')
V_c = OMINSIK.count('V')
E_c = OMINSIK.count('E')

N = int(input())

name_list = []
for i in range(N):
    name = input()
    L=name.count('L') + L_c
    O=name.count('O') + O_c
    V=name.count('V') + V_c
    E=name.count('E') + E_c
    # print(L,O,V,E)
    count = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E))%100
    name_list.append([-count,name])

# print(name_list)
name_list=sorted(name_list,key=lambda x : (x[0],x[1]))
# print(name_list)
print(name_list[0][1])

