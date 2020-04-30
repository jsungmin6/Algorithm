//2칸씩만 움직인다고 가정
var n=20
var s="a B z"
var ssplit=s.split("")
var res
var answer=""
for(var i of ssplit)
{
  if(i!=" ")
  {
    if(i.charCodeAt(0)>="A".charCodeAt(0) && i.charCodeAt(0)<="Z".charCodeAt(0)){
      res = String.fromCharCode((i.charCodeAt(0)+n-"A".charCodeAt(0))%26+"A".charCodeAt(0))
    }else if(i.charCodeAt(0)>="a".charCodeAt(0) && i.charCodeAt(0)<="z".charCodeAt(0)){
      res = String.fromCharCode((i.charCodeAt(0)+n-"a".charCodeAt(0))%26+"a".charCodeAt(0))
    } else {res = String.fromCharCode(i.charCodeAt(0))}
    answer+=res
    res=""
  } else{
    answer+=" "
  }

}
