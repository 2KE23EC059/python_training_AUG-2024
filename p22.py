##Program tp print X shape of N lines
def print_x_shape(n):
    for i in range(n):
        for j in range(n):
            if j == i or j == n - i - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()
n = int(input("Enter the number of lines (odd number): "))
if n % 2 == 0:
    print("Please enter an odd number.")
else:
    print_x_shape(n)