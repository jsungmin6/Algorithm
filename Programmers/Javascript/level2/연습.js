
var arr = [2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 2]

var answer=arr;
var count=1;
var list=[]
var result=1;
while(answer.length!=1){
  var temp=answer[0];
  for(var i=1;i<answer.length;i++)
  {
    if(temp===answer[i]){
      count+=1;
      if(i===answer.length-1)
      {
        list.push(count);
        count=1;
        temp=answer[i];
      }
    }else{
      list.push(count);
      count=1;
      temp=answer[i];
      if(i===answer.length-1)
      {
        list.push(count);
        count=1;
        temp=answer[i];
      }
    }
    }
    answer=list;
    console.log(answer)
    list=[]
    result+=1
}
console.log(result)
