a = [76,46,3,1,4]
min_n = a[0]
max_n = a[0]
for i in range(0,len(a)):
    if a[i] > max_n:
        max_n = a[i]
    else:
        min_n = a[i]

for i in range(0,len(a)):
    if a[i] > min_n and max_n!=a[i]:
        min_n = a[i]
print(min_n)