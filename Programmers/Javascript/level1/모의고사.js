var answers = [1,2,3,4,5];

function solution(answers) {
    var one=[1,2,3,4,5];
    var two=[2,1,2,3,2,4,2,5];
    var three=[3,3,1,1,2,2,4,4,5,5];
    var count1=0, count2=0, count3=0;

    for (var i = 0; i<answers.length ; i++){
        if(answers[i]==one[i%one.length]){
            count1+=1;
        }
    }
    for (var i = 0; i<answers.length ; i++){
        if(answers[i]==two[i%two.length]){
            count2+=1;
        }
    }
    for (var i = 0; i<answers.length ; i++){
        if(answers[i]==three[i%three.length]){
            count3+=1;
        }
    }

    console.log(count1,count2,count3)

    var count=[count2,count3];
    var answer=[count1];
    var score=[1];
    for (var i=0;i<2;i++){
      if (answer[-1]<count[i]){
        score[-1]=i+2;
        answer[-1]=count[i];
      } else if(answer[-1]>count[i]){
        continue;
      } else {
        score.push(i+2);
      }
    }
    console.log(score)




    return score;
}
