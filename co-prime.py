
#The co-prime number definition tells us that if the Greatest Common Factor (GCF) of any two
#numbers is 1, then they are said to be co-prime.Given two numbers a and b print if they are "co-prime" or "Not a co-prime"
def areCoPrime(a, b):
    d = 0
    if a > b:
        x = a
        y = b
    else:
        x = b
        y = a
    while True:
        d = a%b
        if d==1:
            print("co-prime")
            break
        elif d==0:
            print("Not a co-prime")
            break
        else:
            a=b
areCoPrime(56,78)