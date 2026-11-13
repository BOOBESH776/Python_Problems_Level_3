let a = 7
let b = 100
for(let i=a;i<=b;i++){
    let c = 0
    for (let j=1;j<=i;j++){
        if (i%j==0){
            c+=1
        }
    }
    if(c==2){
        console.log(i)
    }
}