def palindrome(name):
    rev= ""
    for i in range(len(name)-1,-1,-1):
        rev+=name[i]
    if name.lower()==rev:
        return "Palindrome"
    else:
        return "Not Plindrome"

print(palindrome("harini"))
