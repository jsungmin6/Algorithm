function collatz(num,k){
    if(num===1)
        {
            return k
        }
    if(num%2===0)
        {
            return collatz(num/2,k+1)
        }
    else{
        return collatz(num*3+1,k+1)
    }
}
console.log(collatz(6,0))
