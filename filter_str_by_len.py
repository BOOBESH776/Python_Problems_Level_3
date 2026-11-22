# Filter Strings by Length: Given an array of strings and an integer L, print only the
# strings whose length is greater than L

a = ["abc","hello","abcdef","qwertyuiop"]
l = 6
for i in range(0,len(a)):
    for j in range(0,len(a[i])):
        if len(a[i]) > l:
            print(a[i])
            break