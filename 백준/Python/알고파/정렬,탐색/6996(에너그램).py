'''
sort 했을 때 같은지 검사
'''

N= int(input());
for _ in range(N):
    A,B=input().split(' ')
    list_A=sorted(list(A));
    list_B=sorted(list(B));
    if list_A==list_B:
        print("{0} & {1} are anagrams.".format(A,B));
    else:
        print("{0} & {1} are NOT anagrams.".format(A,B))