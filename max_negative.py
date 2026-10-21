# Find the Maximum Negative Number in an Array
lst = [-15,-3,8,-10,5,-7]
b = float('-inf')
for i in lst:
    if i < 0 and i > b:
        b=i
print(b)