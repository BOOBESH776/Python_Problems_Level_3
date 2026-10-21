
def count(a,b,c):
    for i in range(0,len(a)):
        if b == a[i]:
            c = c + 1
    if c>=1:
        print(c)
    else:
        print("List not contain that value")
count([8,9,10,10,1,5,18],1,0)