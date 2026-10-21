arr = [5,7,10,9,1,3,4]
b = 9
c = -1
def linear(b,arr,c):
    for i in range(0,len(arr)):
        if arr[i] == b:
            c = i
            break
    return c
print(linear(b,arr,c))
