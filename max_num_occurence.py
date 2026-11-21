a = [3,3,2,2]
c1 = 0
v1 = 0
c2 = 0
v2 = 0
for i in range(0,len(a)):
    v1 = a[i]
    c1 = 0
    for j in range(0,len(a)):
        if a[j] == v1:
            v1 = a[j]
            c1 = c1 + 1
    if c1 > c2:
        v2 = v1
        c2 = c1
print(v2)