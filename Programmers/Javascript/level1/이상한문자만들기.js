var str="try hello world"
/*
answer=str.split(" ").map((a,b)=>{
if(b===0 || b%2===0) return a[b].toUpperCase()
else return a[b].toLowerCase()
})
*/
var answer = ""
var strsplit=str.split(" ")
for (var i of strsplit)
{
  for(var j=0;j<i.length;j++)
  {
    if(j%2===0)
    {
      answer+=i[j].toUpperCase();
    }
    else{
      answer+=i[j].toLowerCase();
    }
  }
  answer+=" "
}
console.log(answer.substring(0,answer.length-1))

function solution(s) {
    var answer = ""
    var strsplit=s.split(" ")
    for (var i of strsplit)
    {
      for(var j=0;j<i.length;j++)
      {
        if(j%2===0)
        {
          answer+=i[j].toUpperCase();
        }
        else{
          answer+=i[j].toLowerCase();
        }
      }
      answer+=" "
    return answer.substring(0,answer.length-1)
}


/*
return s.split(' ').map((word) => word.split('').map((char) => {
    if (small.indexOf(char) > -1) return small[(small.indexOf(char)+n)%small.length]
    else if (big.indexOf(char) > -1) return big[(big.indexOf(char)+n)%big.length]
  }).join('')).join(' ')
}
*/
