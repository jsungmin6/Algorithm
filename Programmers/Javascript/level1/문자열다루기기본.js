function solution(s) {
    var asclist=[];
    var answer=false
    if(s.length==4 || s.length==6)
        {
            for(var i=0;i<s.length;i++)
                {
                    asclist=s.split("").map(x=>x.charCodeAt([0]))
                }
            for(var i=0;i<asclist.length;i++)
            {
            if(asclist[i]<=57 && asclist[i]>=48)
                {
                    answer=true;
                } else {
                    answer=false
                    break
                }

            }
        } else {
            return false
        }
        return answer
}
