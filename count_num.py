a = [3,4,5,2,7,3]
k = 3
c = 0
if a is None:
    print("Invaild")
elif len(a)==0:
    print(c)
else:
    for i in range(0,len(a)):
        if a[i]==k:
            c+=1
    print(c)

