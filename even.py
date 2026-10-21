# Filter All the Even Numbers in an Array

lst = [3,8,12,7,15,20]
b = 0
for i in lst:
    if i % 2 == 0:
        print(i)
        b = b + 1
if b == 0:
    print("No even Number")