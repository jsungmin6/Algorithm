function solution(n) {
    if(n==2){
        return 1
    }

    var count=1
    var s=false
    for(var i = 3; i<=n;i++)
        {
            for(var j=2; j<=i-1; j++)
                {
                    if(i%j==0)
                        {
                           s=false
                           break;
                        }
                    s=true
                }
            if(s){
                count+=1

            }
        }
    return count;
}
