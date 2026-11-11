a = 55678956
b = 18567834
gcd = 1
if a>b:
    c = b
else:
    c = a
for i in range(1,c+1):
    if a%i==0 and b%i==0:
        gcd = i
print(gcd)