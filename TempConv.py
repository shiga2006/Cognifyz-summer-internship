#Task 2: Temperature Conversion
#From Celsius to Fahrenheit
#From Fahrenheit to Celsius
print("1. Celsius to Fahrenheit Conversion")
print("2. Fahrenheit to Celsius Conversion")
ch = int(input("Enter your choice (1/2): "))
if ch==1:
    c = int(input("Enter the Temp in Celsius: "))
    f = (9/5)*c + 32
    print(c,"Degree Celsius is equal to %.2f"%f,"Degree Fahrenheit")
elif ch==2:
    f = int(input("Enter the Temp in Fahernheit: "))
    c = (5/9)*(f - 32)
    print(f,"Degree Fahrenheit is equal to %.2f"%c,"Degree Celsius")
else:
    print("Invalid choice.Check once")
          
