let n = 536
let x = n
let rev = 0
while (n!=0){
    a = n%10
    rev = (rev*10)+a
    b = Math.floor(n/10) 
    n = b
}
console.log(rev)
if (rev == x){
    console.log("Palindrome")
}
else{
    console.log("Not")
}