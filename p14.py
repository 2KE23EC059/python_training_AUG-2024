#Program to find 2nd smallest digit in a number
# Get the user input
user_number = int(input("Enter a positive integer: "))

# Initialize variables to store the smallest and second smallest digits
smallest_digit = float('inf')
second_smallest_digit = float('inf')

# Iterate through each digit in the number
while user_number > 0:
    digit = user_number % 10
    if digit < smallest_digit:
        second_smallest_digit = smallest_digit
        smallest_digit = digit
    elif digit < second_smallest_digit and digit != smallest_digit:
        second_smallest_digit = digit
    user_number //= 10

# Check if a second smallest digit was found
if second_smallest_digit == float('inf'):
    print("There is no second smallest digit in the given number.")
else:
    print(f"The second smallest digit in the number is: {second_smallest_digit}")
