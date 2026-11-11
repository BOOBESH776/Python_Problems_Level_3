a = 26456778345
b = 16875698456
if a < b:
    temp = a
    a = b
    b = temp
while True:
    z = a%b
    if z == 0:
        print(b)
        break
    else:
       a=b
       b=z