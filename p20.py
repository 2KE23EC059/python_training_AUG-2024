#Program to print the Equi Lateral Triangle of N lines
n=int(input("Enter Number of Rows:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()

