# 3. Function Charlie
# Create a function called Charlie
# that accepts a list x and outputs
# the cube root of each number in the list.

def Charlie(input_list):
    return_list = []
    for num in input_list:
        return_list.append(round(num ** (1/3)))

    return return_list


my_list = [1, 8, 27, 64, 125]
print(Charlie(my_list))