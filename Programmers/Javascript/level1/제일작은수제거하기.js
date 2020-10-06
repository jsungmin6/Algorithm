var arr=[1,3,2,4]
console.log(arr.splice(arr.indexOf(Math.min.apply(null,arr)),1))
console.log(arr)

function solution(arr) {
    if(arr.length===1)
        {
            return [-1]
        }else{
            arr.splice(arr.indexOf(Math.min.apply(null,arr)),1)
        }
    return arr;
}
