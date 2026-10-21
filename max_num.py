a = []
if len(a)>0:
    m = a[0]
    for i in range(0,len(a)):
        if m < a[i]:
            m = a[i]
    print(m)
else:
    print("list is empty")