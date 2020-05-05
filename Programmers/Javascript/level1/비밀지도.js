var n=5;
var arr1=[9, 20, 28, 18, 11];
var arr2=[30, 1, 21, 17, 28];
var two1=two(arr1,n);
var two2=two(arr2,n);
var answer=[]
console.log(two1,two2)
for(var i=0;i<n;i++)
{
  var temp=[];
  for(var j=0;j<n;j++)
  {
    if(parseInt(two1[i][j])+parseInt(two2[i][j])==0)
    {
      temp.push(" ")
    }else{
      temp.push("#")
    }
  }
  answer.push(temp.join(""))
}
console.log(answer)


function two(list,n){
  list=list.map(x=>x.toString(2))
  for(var i=0;i<list.length;i++)
  {
    for(var j=list[i].length;j<n;j++)
    {
      list[i]="0"+list[i]
    }
  }
  return list
}
