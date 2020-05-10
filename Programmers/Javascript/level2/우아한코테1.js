var arr = [1, 1, 3, 3, 2, 2, 4, 5, 1, 1, 1, 3, 3, 3]

var answer=arr;
var count=1;
var list=[]
var result=0;
while(answer!=[1]){
  var temp=answer[0];
  for(var i=1;i<answer.length;i++)
  {
    console.log(temp)
    if(temp===answer[i]){
      count+=1;
      if(i===answer.length-1)
      {
        list.push(count);
        console.log(list)
        count=1;
        temp=answer[i];
      }
    }else{
      list.push(count);
      console.log(list)
      count=1;
      temp=answer[i];
    }
    }
    answer=list;
    list=[]
    result+=1
}
