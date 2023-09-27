print("CALCULATOE")
print("1]add")
print("2]sub")
print("3]mul")
print("4]div")
a=input("Enter your choice ")
a=int(a)
n1=input("Enter first number ")
n2=input("Enter seconf number ")
n1=int(n1)
n2=int(n2)
if (a==1):
    print(n1+n2)
elif (a==2):
    print(n1-n2)
elif (a==3):
    print(n1*n2)
elif (a==4):
    print(n1/n2)