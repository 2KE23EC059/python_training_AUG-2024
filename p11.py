#Program to Find Sum of digits of a number
# Get the user input
user_number = int(input("Enter a positive integer: "))

# Initialize a variable to store the sum
total = 0

# Iterate through each digit in the number
while user_number > 0:
    digit = user_number % 10
    total += digit
    user_number //= 10

# Print the result
print(f"The sum of the digits is: {total}")
