var budget=9
var d=[1,1,1,1,1,1,11]

var answer = 0;
var sortd=d.sort();
var money=budget
console.log(sortd)
for(var i=0;i<sortd.length;i++)
    {
        money-=sortd[i]
        if(money>=0)
            {
                answer+=1;
            }else{
                break;
            }
    }
console.log(answer)
