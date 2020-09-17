var value = [
    [3, 7, 9, 2, 7],
    [9, 8, 3, 5, 5],
    [1, 7, 9, 8, 5],
    [3, 8, 6, 4, 10],
    [6, 3, 9, 7, 8]
];
var sum = [];
for (var i = 0; i < value.length; i++) {
    sum[i] = [];
}
sum[0][0] = value[0][0];
var colSum = sum[0][0];
var rowSum = sum[0][0];
for (var i = 1; i < value.length; i++) {
    colSum += value[i][0];
    sum[i][0] = colSum;
}
console.log(sum)

for (var i = 1; i < value.length; i++) {
    rowSum += value[0][i];
    sum[0][i] = rowSum;
}
console.log(sum)

for (var y = 1; y < value.length; y++) {
    for (var x = 1; x < value[0].length; x++) {
        if (sum[y][x - 1] > sum[y -1][x])  {
            sum[y][x] =  sum[y][x - 1]  + value[y][x];
        } else {
            sum[y][x] = (sum[y -1][x] + value[y][x]);
        }
        console.log(sum)
    }

}
console.log(sum[4][4]);
