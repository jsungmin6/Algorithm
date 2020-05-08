var board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
var moves=[1,5,3,5,1,2,1,4]

function solution(board, moves) {
    var e=[]
    var answer = 0;
    for(var i of moves){
      console.log(" i : ",i)
        for(var j of board){
          console.log("j : ",j)
            if(j[i-1]!=0){
                if(e.length>=1 && e[e.length-1]==j[i-1]){
                    e.pop();
                    answer+=2;
                    j[i-1]=0;
                    break;
                }else{
                    e.push(j[i-1])
                    j[i-1]=0;
                    console.log(e)
                    break;
                }
            }
        }

    }
    return answer;
}

console.log(solution(board, moves))
