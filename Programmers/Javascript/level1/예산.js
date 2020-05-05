function solution(d, budget) {
    var answer = 0;
    d=d.sort((a,b)=>a-b)
    var money=0
    for(var i=0;i<d.length;i++)
        {
            money+=d[i]
            if(money<=budget)
                {
                    answer+=1;
                }else{
                    break;
                }
        }

    return answer;
}
