# Find the Maximum Negative Number in an Array
lst = [-15,-3,8,-10,5,-7]
if lst is None:
    print("Invaild")
elif len(lst)==0:
    print("Invaild")
else:
    b = lst[0]
    for i in range(0,len(lst)):
        if b<lst[i] and lst[i]<0:
            b=lst[i]
    print(b)