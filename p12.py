#Program to Find count of digits of a number
# Get the user input
user_number = int(input("Enter a positive integer: "))

# Initialize a variable to store the count
count = 0

# Iterate through each digit in the number
while user_number > 0:
    count += 1
    user_number //= 10

# Print the result
print(f"The number of digits is: {count}")
