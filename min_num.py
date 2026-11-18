a = [8,9,10,1,5,18]
if a is None:
    print("Invaild")
elif len(a)==0:
    print("Invaild")
else:
    b = a[0]
    for i in range(0,len(a)):
        if b<a[i]:
            b=a[i]
    print(b)