a = 12
b = 18
c = a*b
if a<b:
    temp = a
    a = b
    b = temp
while True:
    z = a%b
    if z==0:
        print(b)
        x = c//b
        print(x)
        break
    else:
        a = b
        b = z