# You are given an array of integers. Move all zeros to the end of the array 
# while keeping the original order of the non-zero numbers.
lst = [0, 0, 1]
j=0
for i in range(len(lst)):
    if lst[i] == 0:
        j+=1
for j in range(1,j+1):
    lst.remove(0)
    lst.append(0)
print(lst)