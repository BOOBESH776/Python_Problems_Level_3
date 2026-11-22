
# Minimum and Maximum Difference: Find the difference between the largest and
# smallest elements in an array in a single pass.
a = [8,3,15,2,10]
min_m = a[0]
max_n = [0]
for i in range(0,len(a)):
    if a[i] > max_n:
        max_n = a[i]
    if a[i] < min_n:
        min_n = a[i]
c = max_n - min_n
print(c)