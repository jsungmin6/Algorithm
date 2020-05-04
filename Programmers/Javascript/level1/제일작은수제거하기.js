function solution(arr) {
    if(arr.length===1)
        {
            return [-1]
        }else{
            arr.splice(arr.indexOf(arr.sort()[0]),1)
        }
    return arr;
}
