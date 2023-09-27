# Q)	Reverse a string
s=input("Enter a string ")
c=list(s)
l=len(c)
new_str=""

for i in range(l):
    new_str=new_str+c[l-(i+1)]

print(new_str)