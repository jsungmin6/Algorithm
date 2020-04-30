//2칸씩만 움직인다고 가정

var s="a B z"
var ssplit=s.split("")
var res
var answer=""
for(var i of ssplit)
{
  if(i!=" ")
  {
    if(i.charCodeAt(0)+2>90 && i.charCodeAt(0)+2<97){
      res = String.fromCharCode(i.charCodeAt(0)+2-26)
    }else if(i.charCodeAt(0)+2>122){
      res = String.fromCharCode(i.charCodeAt(0)+2-26)
    } else {res = String.fromCharCode(i.charCodeAt(0)+2)}
    answer+=res
    res=""
  } else{
    answer+=" "
  }

}
console.log(answer)
