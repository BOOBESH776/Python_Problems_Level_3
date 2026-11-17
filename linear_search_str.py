a=[]
k = ""
b = -1
if a is None:
    print("Invaild")
else:
    for i in range(0,len(a)):
        if k == a[i]:
            b=i
            break
    print(b)