genres=["classic", "pop", "classic", "classic", "pop"]	
plays=[500, 600, 150, 800, 2500]

from collections import defaultdict

def solution(genres, plays):
    li = defaultdict(list)
    li_count = defaultdict(int)

    for i in range(len(genres)):
        li[genres[i]].append((plays[i],i))

    for i in range(len(genres)):
        li_count[genres[i]]+=plays[i]

    result_cnt=sorted(li_count.items(),key=(lambda x:-x[1]))

    answer=[]
    for i in result_cnt:
        k = i[0]
        k_li=li[k]
        k_li=sorted(k_li,key=lambda x:(-x[0],x[1]))
        if len(k_li) ==1:
            answer.append(k_li[0][1])
        else:
            answer.append(k_li[0][1])
            answer.append(k_li[1][1])
            
    return answer