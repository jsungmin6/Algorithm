var arr = [123, 234, 213, 432, 234, 1234, 2341, 12345, 324];
var list =[]
var count=1
for(var i=0;i<arr.length;i++){
  var temp=String(arr[i]).split("").sort().join("")
  list.push(temp)
}
console.log(list)
var answer=list.sort();
console.log(answer)
var first=answer[0]
var result=[]
for (var i=1;i<answer.length;i++){
  {
    if(first===answer[i]){
      count+=1;
      if(i===answer.length-1)
      {
        result.push(count);
      }
    }else{
      result.push(count);
      count=1;
      first=answer[i];
      if(i===answer.length-1)
      {
        result.push(1);
      }
    }
    }
}
console.log(result)
