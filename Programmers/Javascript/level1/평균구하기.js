function solution(arr) {
    var answer = arr.reduce((accu, curr) => accu + curr)
    return answer / arr.length;
}
