
var heights=[6,9,5,7,4];
var answer = [];
var key;
for(var i=heights.length-1;i>0;i--)
    {
      key=0;
      console.log("i :", heights[i])
        for(var j=i-1;j>=0;j--)
            {
              console.log("J :", heights[j])
                if(heights[j]>heights[i])
                    {
                        answer.unshift(j+1)
                        key=1
                        break
                    }
            }
        if(key===0)
        {
          answer.unshift(0);
          key=1;
        }
    }
console.log(answer)
