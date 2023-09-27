# Q)Count number of vowels in a string
s=input("Enter a word ")
s.lower()
print(s)
l=0
for k in s:
    if ((k=="a")or(k=="e")or(k=="i")or(k=="o")or(k=="u")):
        l=l+1
print(l)