function solution(n) {
    var watermelon="수박"
    var answer=""
    for(var i=0;i<parseInt(n/2);i++)
        {
          answer+=watermelon
        }
    if(n%2==1)
        {
         answer+="수"
        }
    return answer;
}
