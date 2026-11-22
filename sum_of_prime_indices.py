# Sum of Prime Indices: Calculate the sum of elements located at prime-numbered
# indices (2, 3, 5, 7, ...) in an array

a = [2,3,5,7,8]
s = 0
for i in range(0,len(a)):
    c = 0
    for j in range(1,a[i]+1):
        if a[i]%j==0:
            c+=1
    if c==2:
        s = s + a[i]
print(s)