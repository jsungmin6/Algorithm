function solution(x) {
    var answer = (x+"").split("").map(x=>parseInt(x)).reduce((a,b)=>a+b)
    if(x%answer==0){
        return true
    } else{
        return false
    }
}
