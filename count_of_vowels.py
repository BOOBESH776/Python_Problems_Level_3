def vowel(s):
    c = 0
    for i in range(len(s)):
        if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
            c=c+1
    print("count of vowels:",c)
a = "AbCde"
s = a.lower()
vowel(s)