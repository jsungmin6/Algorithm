data=[2,1,5,1,2,2,2]
M=5
K=3

lo = 0
hi = sum(data)

while lo+1 < hi: #lo와 hi 사이에 한개는 있을 때 수행해야 함.
    mid = (lo+hi)//2
    sum = 0
    currentBlockSum = 0;
    block = 1;

    for number in data:
        currentBlockSum += number;

        # // If currentBlockSum > midpoint means that we are
        # // in a different block...
        if currentBlockSum > midpoint:
            ++block;

            # // ...so we reset sum with the current number
            currentBlockSum = number;

            # // but if we are out of blocks, our guess (midpoint) is incorrect
            # // and we will have to adjust it
            if block > numberOfBlocks:
                brea
    # // If we are out of blocks
    # // it means that our guess (midpoint) is bigger than we thought
    if block > numberOfBlocks:
        begin = midpoint + 1;
    # // else, it's smaller
    else:
        result = midpoint;
        end = midpoint - 1
