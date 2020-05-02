var n=5, lost=[2,3],reserve=[3,4];

function solution(n, lost, reserve) {
    var answer=n-lost.length;
    var count=0;
    for (var i of lost)
        {
            if(reserve.includes(i-1))
                {
                  console.log('i-1',i-1)
                    count+=1;
                    reserve.splice(reserve.indexOf(i-1),1);
                    console.log(reserve)
                } else if(reserve.includes(i+1)){
                  console.log('i+1',i+1)
                    count+=1;
                    reserve.splice(reserve.indexOf(i+1),1);
                    console.log(reserve)
                }
        }
    return answer+count
}

console.log(solution(n, lost, reserve));
