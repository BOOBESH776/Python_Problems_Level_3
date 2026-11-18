let a = [3,5,1,7,3,8]
if (a==null){
    console.log("Invaild")
}
else if(a.length==0){
    console.log("Invaild")
}
else{
    let b = a[0]
    //max Number
    for(let i=0;i<=a.length;i++){
        if (b<a[i]){
            b=a[i]
        }
    }
    console.log(b)

    //Min number
    for(let i=0;i<=a.length;i++){
        if (b>a[i]){
            b=a[i]
        }
    }
    console.log(b)
}