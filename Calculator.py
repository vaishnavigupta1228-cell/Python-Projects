def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
print("Please select your choice:\n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")
sel=int(input("Select your choice(1-4): "))
if sel==1:
   n1=float(input("Enter first number:"))
   n2=float(input("Enter second number:"))
   print(n1,"+",n2,"=",add(n1,n2))
elif sel==2:
    n1=float(input("Enter first number:"))
    n2=float(input("Enter second number:"))
    print(n1,"-",n2,"=",sub(n1,n2))
elif sel==3:
    n1=float(input("Enter first number:"))
    n2=float(input("Enter second number:"))
    print(n1,"*",n2,"=",mul(n1,n2))
elif sel==4:
    n1=float(input("Enter first number:"))
    n2=float(input("Enter second number:"))
    if n2==0:
        print("Error Division by zero!")
    else:
        print(n1,"/",n2,"=",div(n1,n2))
else:
    print("Invalid choice")
    
