
import re

def check_password_complexity(password):
    # Define the complexity criteria
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Calculate the number of criteria met
    complexity_score = sum([length_criteria, lowercase_criteria, uppercase_criteria, digit_criteria, special_char_criteria])

    # Define the messages for the password check
    if complexity_score == 5:
        return "Password is very strong."
    elif complexity_score == 4:
        return "Password is strong."
    elif complexity_score == 3:
        return "Password is moderate."
    elif complexity_score == 2:
        return "Password is weak."
    else:
        return "Password is very weak."

# Test the password complexity checker
password = input("Enter a password to check its complexity: ")
result = check_password_complexity(password)
print(result)



