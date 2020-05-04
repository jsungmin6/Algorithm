var n = 182475

var nlist=String(n).split("").map(x=>x=parseInt(x)).sort(function(a, b) {
  return b - a;
}).join("")

console.log(nlist)
