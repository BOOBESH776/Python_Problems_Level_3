def bi(a,k):
    low = 0
    high = len(a)
    k = "b"
    ans = -1
    while low<=high:
        mid = (low+high)//2
        if k==a[mid]:
            ans = mid
            return ans
        elif k>=a[mid]:
            low = mid + 1
        elif k<=a[mid]:
            high = mid - 1
    return ans
print(bi(["a","b","c","d","e","i","x","z"],"b"))



