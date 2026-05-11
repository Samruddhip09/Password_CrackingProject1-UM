import re

def check_strength(password):
    if len(password) < 6:
        return "Weak"
    elif re.search("[A-Z]", password) and re.search("[0-9]", password):
        return "Strong"
    else:
        return ("Medium")

print(check_strength("Admin123"))