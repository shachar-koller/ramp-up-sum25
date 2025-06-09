# 2. Function Bravo
# Create a function called Bravo that
# uses a for loop to return the total
# of the numbers 1 through 10.

def Bravo():
    total = 0
    for i in range(1,11):
        total += i
    return total

print(Bravo())