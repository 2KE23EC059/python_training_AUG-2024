#Program to Find Odd(Even) placed digits in a number
num = int(input("Enter a positive integer: "))
sum_even = 0
sum_odd = 0
position = 1
while num > 0:
    digit = num % 10
    if position % 2 == 0:
        sum_even += digit
    else:
        sum_odd += digit
    num //= 10
    position += 1
print(f"Sum of odd-placed digits: {sum_odd}")
print(f"Sum of even-placed digits: {sum_even}")
