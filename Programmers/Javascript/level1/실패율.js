var N=15;
var stages=[12,12,12,12,12,6,6]

function solution(N, stages) {
    var all=stages.length
    var temp=[]
    for(var i=1;i<=N;i++)
        {
            if(all!=0){
                var ct=count(i,stages);
                temp.push([i,ct/all])
                all-=ct
            } else{
              temp.push([i,0])
            }

        }
    console.log(temp)
    var answer=temp.sort(function(x,y){if(x[1]===y[1]){return 1;}
    return y[1]-x[1]})
    console.log(answer)
    var list=[];
    for(var i of answer){
      list.push(i[0])
    }
    return list
}

console.log(solution(N,stages))

function count(num,list){
    var count=0
    for(var i of list)
        {
            if(i===num){
                count+=1
            }
        }
    return count
}
