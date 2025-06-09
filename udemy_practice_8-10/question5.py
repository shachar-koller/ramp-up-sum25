import random

# 5. Function Echo
# Create a function called
# Echo that outputs 20 random
# numbers to a file called theFile.txt.

def Echo():
    results = []
    for i in range (20):
        random_num = random.randint(0, 1000)
        results.append(random_num)
    try:
        f = open("theFile.txt", "x")
    except FileExistsError:
        pass

    with open("theFile.txt", "w") as file:
        input = ("\n".join(str(num) for num in results))
        file.write(input)

Echo()