# Question 8 - Favorite Color (switch statement)
# Do the same as above, but use a switch statement.
# Present the choices as:
# - blue
# - red
# - green

def color_switch(color):
    if color == 'blue':
        print('Great choice.')
    elif color == 'red':
        print('Poor choice.')
    elif color == 'green':
        print('Not a bad choice.')
    else:
        print('Sorry, that\'s not a primary color.')

color_switch(input("Enter your favorite color\nIt should be either blue, red or green:\n"))