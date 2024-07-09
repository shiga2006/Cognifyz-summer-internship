#Task 5: Palindrome checker
#Using slicing
string = input("Enter the string: ")
reverse_string = string[::-1]
if string == reverse_string:
    print("String is a palindrome")
else:
    print("String is not a palindrome")
