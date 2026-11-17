let a = ["abc","e","f","d","j","j"]
let b =-1
let key = "j"
if (a == null){
console.log("Invaild")
}
else if (a.length==0){
    print(b)
}
else{
    for(let i = 0;i<=a.length;i++){
        if(a[i]==key){
            b = i
            break
        }
    }
    console.log(b)
}