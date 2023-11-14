print("SIMPLE CALCULATOR")
n1=float(input("Enter first number:"))
n2=float(input("Enter second number:"))
print("Press")
print("1 for Addition")
print("2 for Subtraction")
print("3 for multiplication")
print("4 for division")
op=int(input("enter your choice"))
if op==1:
  print("The addition of 2 entered number is",n1+n2)  
elif op==2:
  print("The subtraction of 2 entered number is",n1-n2)
elif op==3:
 print("The multiplication of 2 entered number is",n1*n2)
elif op==4:
     if n2==0:
       print("Error")
     elif n2>0:
          print("The division of 2 entered number is",n1/n2)
else:
  print("INVALID INPUT")