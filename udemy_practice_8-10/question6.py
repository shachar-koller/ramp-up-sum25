# Question 6 - Function Foxtrot
# Create a function called Foxtrot that takes in a float number and returns number * 2.
# Use this function in main to output the powers of 2 from 2⁰ through 2¹⁰.

def Foxtrot(floaty):
    
    return_var = float(floaty) * 2.0

    return return_var

def main():
    result = 1.0
    print(f"_____________________________________")
    print(f"The powers of 2 from 2^0 until 2^10")
    print(f"-------------------------------------")
    for i in range(11):
        print(int(result))
        result = int(Foxtrot(result))

main()