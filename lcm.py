a = 5
b = 8
if a>b:
    c = a
    i = a
    d = b
else:
    c = b
    i = b
    d = a
while True:
    i = i + c
    if i%d==0:
        print(i)
        break
