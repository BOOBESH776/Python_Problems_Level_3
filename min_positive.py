# You are given an array of integers. Find and print the minimum positive number,
# which is the positive number closest to zero. If there are no positive numbers, print No positive numbers.
pn = [65,76,7,24,6,1]
m = pn[0]
c=0
for i in range(len(pn)):
    if pn[i]>0 and m > pn[i]:
        m=pn[i]
        c+=1
if c==0:
    print("No positive number")
else:
    print(m)