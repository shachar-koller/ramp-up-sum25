# 3. Password Validation
# Ask the user to create a password that meets the following criteria:
# At least 8 characters long
# Contains a number
# Contains an uppercase letter
# Contains a lowercase letter
# Contains a special character
# If the password is invalid, tell them which specific requirement is not met.
# Give them unlimited attempts to get it correct.

def has_numbers(input):
    return any(char.isdigit() for char in input)

def has_chars(input):
    return any(char.isalpha() for char in input)

def has_upper(input):
    return any(char.isupper() for char in input)

def has_lower(input):
    return any(char.islower() for char in input)

def has_special(input):
    special_characters = "\"!@#$%^&*()-+?_=,<>\""
    return any(char in special_characters for char in input)

passwordNotFound = True
while passwordNotFound:
    user_password = input("Please create a password which is at least 8 characters long, contains a number, contains an uppercase letter, contains a lowercase letter, and contains a special character\n")
    if len(user_password) < 8:
        print("too short")
        continue
    if not has_chars(user_password):
        print("missing characters")
        continue
    if not has_numbers(user_password):
        print("missing numbers")
        continue
    if not has_upper(user_password):
        print("missing uppercase")
        continue
    if not has_lower(user_password):
        print("missing lowercase")
        continue
    if not has_special(user_password):
        print("missing special char")
        continue
    passwordNotFound = False

print("Your password has been created successfully!")

