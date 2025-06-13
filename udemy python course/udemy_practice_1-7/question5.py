# 5. Even Numbers Backwards
# Use a while loop to output all the even numbers between 1 and 100, in reverse order, like this:
# 100, 98, 96, ...

i = 100
final = []
while True:
    if i == 0:
        break
    to_append = str(i) + ", "
    final.append(i)
    i -= 2

print(", ".join(str(num) for num in final))