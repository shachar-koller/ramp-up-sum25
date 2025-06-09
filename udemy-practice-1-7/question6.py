# 6. Prime Numbers from 100 to 1000
# Use a loop to output all prime numbers between 100 and 1000.
# Separate the numbers with a bar |, like this:
# 101 | 103 | 107 | ...

def finding_primes(lower_bound, upper_bound):
    all_nums = 2
    prime = True
    results = []

    for num_to_check in range (lower_bound, upper_bound):
        prime = True
        all_nums = 2
        while all_nums < num_to_check:
            if num_to_check % all_nums == 0:
                prime = False
                break
            all_nums += 1
        if prime:
            results.append(num_to_check)
    
    return("| ".join(str(num) for num in results))

def main():
    print(finding_primes(100, 1000))

main()