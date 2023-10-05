# Q)Calculator using Class
class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(num1,num2):
        return num1+num2
    def sub(num1,num2):
        return num1-num2
    def mul(num1,num2):
        return num1*num2
    def div(num1,num2):
        return num1/num2
    
print("CALCULATOE")
print("1]add")
print("2]sub")
print("3]mul")
print("4]div")
a=input("Enter your choice")
a=int(a)

n1=input("Enter first number")
n2=input("Enter seconf number")
n1=int(n1)
n2=int(n2)
if (a==1):
    print(f"Answer is {Calculator.add(n1,n2)}")
    
elif (a==2):
    print(f"Answer is {Calculator.sub(n1,n2)}")

elif (a==3):
    print(f"Answer is {Calculator.mul(n1,n2)}")

elif (a==4):
    print(f"Answer is {Calculator.div(n1,n2)}")