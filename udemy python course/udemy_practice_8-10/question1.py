# 1. Function Alpha
# Create a function called Alpha that takes in a number
# and uses a while loop to count from 1 to that number,
# inclusive. The function should output each number to the console.

def Alpha(number):
    counter = 1
    while counter <= number:
        print(counter)
        counter += 1


Alpha(100)