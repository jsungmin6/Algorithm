var m=12
var n=3;
var nlist=[];
var mlist=[];
for (var i=1;i<=n;i++)
    {
        if(n%i===0)
            {
                nlist.push(i)
            }
    }
for (var i=1;i<=m;i++)
    {
        if(m%i===0)
            {
                mlist.push(i)
            }
    }

var g=nlist.filter(x=>mlist.includes(x))
var k=Math.max(...g)
var l=m*n/k
console.log(k,l)
