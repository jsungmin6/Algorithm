var N=5;
var stages=[2, 1, 2, 6, 2, 4, 3, 3]
function solution(N, stages) {
    let ans = []

    for (let i = 1; i <= N; ++i) {
        let usersReachedCurrentStage   = stages.reduce((acc, curStage) => acc + ((curStage >= i) ? 1 : 0), 0)
        console.log("usersReachedCurrentStage : " + usersReachedCurrentStage)
        let usersStagnatedCurrentStage = stages.reduce((acc, curStage) => acc + ((curStage == i) ? 1 : 0), 0)
        console.log("usersStagnatedCurrentStage : " + usersStagnatedCurrentStage)
        if (usersReachedCurrentStage === 0) {
            ans.push({ 'stage': i, 'failRate': 0 })
            console.log(ans)
            continue
        }

        ans.push({ 'stage': i, 'failRate': (usersStagnatedCurrentStage / usersReachedCurrentStage) })
        console.log(ans)
    }

    return ans.sort((a, b) => {
        if (a.failRate > b.failRate) return -1
        if (a.failRate < b.failRate) return 1
        return a.stage - b.stage
    }).map(entry => entry.stage)
}
solution(N,stages)
