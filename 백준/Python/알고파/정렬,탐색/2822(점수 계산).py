scores=[]
for i in range(8):
    scores.append([int(input()),i+1])

scores=sorted(scores,reverse=True)

scores_sum=0
scores_list=[]
for i in range(5):
    scores_sum+=scores[i][0]
    scores_list.append(scores[i][1])

scores_list.sort()
print(scores_sum)
print(*scores_list)
