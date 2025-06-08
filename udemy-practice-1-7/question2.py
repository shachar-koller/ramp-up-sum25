# 2. Name and Age Validation
# Ask a user for their name and age.
# Ensure that they give letters for their name.
# Ensure that they give numbers for their age.
# Ensure that the age is between 1 and 100, inclusive.
# Give them three chances to provide valid input.
# If they fail after three attempts, output:
# "Unacceptable"
# If both name and age are valid, output:
# "Acceptable"

ATTEMPTS_ALLOWED = 3
name_and_age_valid = False

for i in range(ATTEMPTS_ALLOWED):
    name = input("What is your name? ")
    age = (input("How old are you? "))
    if not name.isalpha():
        print("Name invalid. Only letters allowed")
        continue
    try:
        age_int = int(age)
    except ValueError:
        print("Age invalid. Only integers allowed")
        continue
    if not (1<= age <= 100):
        print("Age invalid. Integers between 1 and 100 only")
        continue
    name_and_age_valid = True
    break


if not name_and_age_valid:
   print("Unacceptable")
else:
    print("Acceptable")