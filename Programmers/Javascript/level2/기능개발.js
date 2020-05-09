var progresses=[93,30,55];
var speeds=[1,30,5];

function solution(progresses, speeds) {
    var daylist=[];
    var count=1;
    var day=0;
    var answer=[];
    for(var i=0;i<progresses.length;i++)
        {
            day=Math.ceil((100-progresses[i])/speeds[i])
            daylist.push(day)
        }
    var key=daylist[0];
    for(var i=1;i<daylist.length;i++)
        {
            if(key>=daylist[i]){
                count+=1;
            }else{
                answer.push(count)
                count=1;
                key=daylist[i]
            }

        }
    answer.push(count)
    return answer;
}
console.log(solution(progresses, speeds))
