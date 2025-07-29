s = "UEM"
rev = ""  
for char in s:
    rev = char + rev
if s == rev:
    print("Yes the given expression was Palindrome")
else:
    print("No the given expression was not Palindrome")
#Output :- No