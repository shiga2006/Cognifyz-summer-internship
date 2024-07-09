#Level 2
#Task 4:Fibonacci Series
num = int(input("Enter any number: "))
n1, n2 = 0, 1
sum = 0
if num <= 0:
    print("Please enter no greater than 0")
else:
    for i in range(0, num):
        print(sum, end=" ")
        n1 = n2
        n2 = sum
        sum = n1 + n2
    
