#Check if a number is Prime
n = int(input("Enter a number: "))
if n > 1:
    for i in range(2, n // 2):
        if (n % i) == 0:
            print(f"{n} is not a prime number")
            break
