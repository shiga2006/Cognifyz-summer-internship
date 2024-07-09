#Task 3:Email Validator
import re

pattern = "^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

email_id = input("Enter your email id: ")

if re.search(pattern, email_id):
    print(f"{email_id} is valid.")
else:
    print(f"{email_id} is invalid.")

