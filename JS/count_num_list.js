let a = [3,4,5,2,7,3]
let k = 3
let c = 0
if (a == null){
    console.log("Invaild")
}
else if (a.length==0){
    console.log(c)
}
else{
    for (let i=0;i<=a.length;i++){
        if (a[i]==k){
            c+=1
        }
    }
    console.log(c)
}