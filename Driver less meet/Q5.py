# Q)Find largest element in array
a=input("Enter the number of elements in the list ")
l=[]
for i in range(int(a)):
    temp=input(f"Enter the {i+1} element ")
    l.append(int(temp))
print(l)
print(max(l))