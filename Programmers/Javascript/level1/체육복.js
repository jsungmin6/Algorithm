var n=5, lost=[2,3],reserve=[3,4];

function solution(n, lost, reserve) {
    var newlost = lost.filter(x => !reserve.includes(x));
    var newreserve = reserve.filter(x => !lost.includes(x));
    var answer=n-newlost.length;
    var count=0;
    for (var i of newlost)
        {

            if(newreserve.includes(i-1))
                {
                    count+=1;
                    newreserve.splice(newreserve.indexOf(i-1),1);
                } else if(newreserve.includes(i+1)){
                    count+=1;
                    newreserve.splice(newreserve.indexOf(i+1),1);
                }
        }
    return answer+count
}

console.log(solution(n, lost, reserve));
