function solution(n) {
    var arr=[0]
    for(var i=1; i<=n; i++){
      arr[i]=i
    }

    for (let i = 2; i <= n; i++) { // 1은 소수제외. 2부터 시작
      if (arr[i] === 0) continue; // 배수 0 체크한 수는 skip
      for (let j = i + i; j <= n; j += i) {
        arr[j] = 0; // n의 배수는 0 채움.
      }
    }
    return arr.filter(v => v > 1).length
}
