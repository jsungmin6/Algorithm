function solution(n)
{
    var answer = 0;
    var s=n.toString(10)
    for(var i=0;i<s.length;i++)
        {
            answer+=parseInt(s[i])
        }

    return answer;
}
