p = 
a = 0
def prime(p,a):
    for i in range(1,p+1):
        if p%i==0:
            a+=1
    if a==2:
        return "prime"
    else:
        return "Not"

print(prime(p,a))