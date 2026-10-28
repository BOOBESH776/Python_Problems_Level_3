# Find the Min Negative Number in an Array
lst = [10,-4,-2,5,-6]
a = 0
b=lst[0]
for i in range(0,len(lst)):
    if lst[i] < 0 and lst[i] < b:
        b = lst[i]
print(b)