var n=12345;
n=String(n);
var nlist=n.split("").reverse();

var answer=[];
for (var i of nlist){
  answer.push(parseInt(i));
}

console.log(answer)
