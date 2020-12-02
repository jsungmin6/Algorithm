N = int(input())
dragons = list(map(int, input().split()))

result = 0
for i in range(len(dragons)):
    if len(dragons)-i < result:
        break
    count = 0
    for j in dragons[i+1:]:
        if dragons[i] > j:
            count += 1
            if j == dragons[-1]:
                result = max(result, count)
        else:
            result = max(result, count)
            break

print(result)
