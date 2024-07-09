#Level 2
#Task 3: Password Strength Checker
def check_password_strength(password):

    special_chars = list('@#$%&*')
    isdigit_there = any(char.isdigit() for char in password)
    isupper_there = any(char.isupper() for char in password)
    isspchar_there = any(char.isdigit() for char in password)
    check_lower = any(char.islower() for char in password)

    all_true = all([isdigit_there, isupper_there, isspchar_there, check_lower])
    if len(password) < 6:
        return "Weak"
    elif len(password) >= 8 and all_true:
        return "Strong"
    else:
        return "Average"


user_password = input("Enter your password: ")
strength = check_password_strength(user_password)
print("")
print("Your password is {} !!".format(strength))
