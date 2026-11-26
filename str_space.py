# Given a string str, write a program to print all words with even length in the given string. 
# Assume each word is separated by a single SPACE

a = "hi iam vidya studying twelfth"
c = 0
rev = ""
str = ""
for i in a:
  if i!=" ":
    c = c+1
    rev = rev + i
  else:
    if c%2==0:
      str = str + rev + ","
    rev = ''
    c = 0

if c%2==0:
  str += rev 
print(str)
      