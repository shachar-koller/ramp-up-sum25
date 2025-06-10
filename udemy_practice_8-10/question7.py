# Question 7 - Favorite Color (if/else)
# Ask the user for their favorite color.
# Store it in a variable named color.
# 
# If they choose "blue" → output "Great choice."
# If "red" → output "Poor choice."
# If "green" → output "Not a bad choice."
# Otherwise → output "Sorry, that's not a primary color."
# 
# Use an if / else-if / else statement.

color = input("Enter your favorite color:\n")

if color.lower().strip() == 'blue':
    print("Great choice.")
elif color.lower().strip() == 'red':
    print("Poor choice")
elif color.lower().strip() == 'green':
    print("Not a bad choice.")
else:
    print("Sorry, that's not a primary color.")