import pdb # import the pdb module

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1

    result = 1
    pdb.set_trace() # Start debugging from here
    
    for i in range(1, n + 1):
        result *= i
        print(f"Intermediate result for i={i}: {result}") 
    return result

print("--- PDB Debugging Example ---")

try:
    # Add pdb here and try
    # pdb.set_trace()

    num_factorial = 5
    fact_result = factorial(num_factorial)
    print(f"The factorial of {num_factorial} is: {fact_result}")

    # negative_num = -3
    # fact_negative = factorial(negative_num)
    # print(f"The factorial of {negative_num} is: {fact_negative}")

except ValueError as e:
    print(f"Error: {e}")

