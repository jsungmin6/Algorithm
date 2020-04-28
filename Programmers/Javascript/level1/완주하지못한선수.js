//완주자가 여러명일 경우
function solution(participant, completion) {
    var index
    for(var i of completion)
        {
            participant.splice(participant.indexOf(i),1);
        }
    return participant
}

//완주 못한 자가 한명일 경우.
function solution(participant, completion) {
    participant.sort();
    completion.sort();

    for(let i in participant) {
        if(participant[i] !== completion[i]) return participant[i];
    }
}
