import re

def check_password_strength(password):
    
    if len(password) < 8:
        return "Password must be at least 8 characters long."

    if not re.search("[A-Z]", password):
        return "Password must contain at least one uppercase letter."

    if not re.search("[a-z]", password):
        return "Password must contain at least one lowercase letter."

    if not re.search("[0-9]", password):
        return "Password must contain at least one number."

    if not re.search("[@#$%^&*()_+!]", password):
        return "Password must contain at least one special character."

    return "Password is strong."

# User input
password = input("Enter your password: ")

result = check_password_strength(password)
print(result)