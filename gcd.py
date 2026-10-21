a = 18
b = 24
if a > b:
    x = a
    y = b
else:
    x = b
    y = a
while True:
    z = x%y
    if z == 0:
        print(y)
        break
    else:
        x = y
        y = z