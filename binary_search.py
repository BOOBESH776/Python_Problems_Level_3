num = [5,6,8,10,25,78,90,91]
start = 0
end = len(num)-1
key=1
while start<=end:
  mid = (start+end)//2
  if num[mid]==key:
    print(mid)
    break
  elif num[mid]<key:
    start = mid+1
  elif num[mid]>key:
    end = mid-1