const a = [-3,-1,-7,-1,0]
let max_n = a[0]
let min_n = a[0]
for(let i=0;i<a.length;i++){
    if (a[i] > max_n){
        max_n = a[i]
    }
    else{
        min_n = a[i]
    }
}
for(let j=0;j<a.length;j++){
    if (a[j]>min_n && a[j]!=max_n){
        min_n = a[j]
    }
}
console.log(min_n);