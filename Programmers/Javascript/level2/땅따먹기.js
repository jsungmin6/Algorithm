var land = [[1,1,1,1,],[2,1,1,1],[1,1,1,1]]

var max=0
var index=-2
var answer=0;
for(var i=0;i<land.length;i++){
  if(index!=land[i].indexOf(Math.max(...land[i]))){
    max=Math.max(...land[i])
    index=land[i].indexOf(max)
    answer+=max;
  } else{
    land[i][land[i].indexOf(Math.max(...land[i]))]=0;
    index=land[i].indexOf(Math.max(...land[i]))
    answer+=Math.max(...land[i]);
  }

}
console.log(land)
console.log(answer);
