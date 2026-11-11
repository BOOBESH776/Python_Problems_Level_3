a = [7,26,48]
b = a[0]
gcd = 1
c = 0
for i in range(len(a)):
    if b > a[i]:
        b = a[i]
for i in range(1,b+1):
    for j in range(len(a)):
        if a[j]%i==0:
            c +=1
    if c==len(a):
        gcd = i
    else:
        c=0
print(gcd)