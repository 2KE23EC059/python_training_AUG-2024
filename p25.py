#Assume 1 and 2 are 1st 2 terms of the series and print the 1st N term of Fibo series (HemaChandra numbers)
N = int(input("Enter the number of terms for the Fibonacci series: "))
a, b = 1, 2
print(a, b, end=" ") 
for _ in range(N - 2):  
    c = a + b
    print(c, end=" ")
    a, b = b, c
