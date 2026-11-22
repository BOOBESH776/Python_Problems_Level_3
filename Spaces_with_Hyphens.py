#  Replace Spaces with Hyphens: Traverse a string and replace every space character
# with a hyphen (-).
s = "  a b c  "
b = ""
c = "-"
for i in range(0,len(s)):
    if s[i] == " ":
        b = b + c
    else:
        b = b + s[i]
print(s)
print(b)