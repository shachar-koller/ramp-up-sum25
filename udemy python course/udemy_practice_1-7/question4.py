# 4. Numbers with the Digit "3"
# Use a for loop to output every number between 1 and 1000 that contains the digit 3.
# Separate the numbers with a bar |, like this:
# 3 | 13 | 23 | ...

results = []
for i in range (1001):
    string_representation = str(i)
    if "3" in string_representation:
        results.append(str(i))
final_output = "|".join(results)
print(final_output)