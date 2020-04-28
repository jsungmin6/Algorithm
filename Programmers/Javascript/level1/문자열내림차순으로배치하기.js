function solution(s) {
    var ascii=[]
    var answer=""

    for(var i=0;i<s.length;i++){
      ascii.push(s.charCodeAt([i]));
    }

    console.log(ascii)

    ascii.sort(function (a, b) {return b-a})

    for(var i=0;i<ascii.length;i++){
      answer+=String.fromCharCode(ascii[i])
    }
    return answer
}
