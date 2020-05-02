var n=5, lost=[2,4],reserve=[1,3,5];

function solution(n, lost, reserve) {
    var answer=n-lost.length;
    var count=0;
    for (var i of lost)
        {
            if(i-1 in reserve)
                {
                    count+=1;
                    reserve.splice(reserve.indexOf(i-1),1);
                } else if(i+1 in reserve){
                    count+=1;
                    reserve.splice(reserve.indexOf(i+1),1);
                }
        }
    return answer+count
}
console.log(solution(n, lost, reserve));
