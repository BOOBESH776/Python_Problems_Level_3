# Count Digits in a String: Given an alphanumeric string, count how many characters are
# numeric digits (0-9).
s = "hello 123"
c = 0
if s is None:
    print("Invaild")
for i in range(0,len(s)):
    if 'a'<=s[i]<='z' or 'A' <= s[i] <= 'Z' or s[i]==" ":
        pass
    else:
        c+=1
print(c)