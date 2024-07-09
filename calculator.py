#Task 4:Calculator Program
print("Choose an operator:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
option = int(input("Choose an option: "))
result=0

if(option in [1,2,3,4]):
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))

    if(option==1):
        result = num1 + num2
    elif(option==2):
        result = num1 - num2
    elif(option==3):
        result = num1 * num2
    elif(option==4):
        result = num1//num2

else:
    print("Invalid option.")
   
        
print("The result of the operation is {}".format(result))
