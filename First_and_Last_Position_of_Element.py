# a = [1,1,1,1,2,3,22,22,22,22,45,45,45,55]
# low = 0
# high = len(a)
# s = 0
# e = 0
# k = 1
# mid = (low+high)//2
# for i in range(mid,-1,-1):
#   if k==a[i]:
#     for j in range(i,-1-1):
#       if k==a[j]:
#         s = j
#       else:
#         break
# for x in range(s,len(a)):
#   if k==a[x]:
#     for y in range(x,len(a)):
#       if k==a[y]:
#         e = y
#       if s==0:
#         s = y
#       else:
#         break
# if e<0:
#   e = j
# print(s,e)

# a = [1,1,1,1,2,3,22,22,22,22,45,45,45,55]
# low = 0
# high = len(a)
# k = 1
# s = -1
# e = -1
# while low<=high:
#   mid = (low+high)//2
#   if k==a[mid]:
#     s = mid
#     high = mid - 1
#   break
    
# low = 0
# high = len(a)-1
# while low<=high:
#   mid = (low+high)//2
#   if k==a[mid]:
#     e = mid
#     low = mid + 1
#   break
# print(s,e)
    
a = [1,2,3,4,5,5,5,5,5,5,6,8,9,10]
k = 8
s = -1
e = -1

for i in range(len(a)):
    if a[i] == k:
        if s == -1:
            s = i  
        e = i

print(s, e)

