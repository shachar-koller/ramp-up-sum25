# 4. Function Delta
# Create a function called Delta that uses a while
# loop to ask the user for their age until they give
# an age between 0 and 100, inclusive.
# The function should return the variable age to main.
# Show how this function is called in main.

def Delta():
    age_gotten = False
    while not age_gotten:
        try:
            age = int(input("Input your age: "))
        except ValueError:
            continue
        if 0 <= age <= 100:
            return age
        else:
            continue

def main():
    age = Delta()
    print(age)

main()