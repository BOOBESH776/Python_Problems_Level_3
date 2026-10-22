# Find the max number of count
def max(a):
    m = a[0]
    c = 0
    for i in range(len(a)):
        if m < a[i]:
            m = a[i]
    print("max number :",m)
    for j in range(len(a)):
        if m == a[j]:
            c += 1
    print("Count of max :",c)
max([1,4,2,7,7,2,7])