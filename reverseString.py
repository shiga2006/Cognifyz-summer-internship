def reverse(string):
    reversed_string = ""
    for i in string:
        reversed_string = i + reversed_string
    print("Reversed String is ", reversed_string)

user_string = input("Enter a string: ")
print("Entered string", user_string)
reverse(user_string)
