#program to accept 3 distinct numbers and find smallest among them
x = int(input("enter first number:"))
y = int(input("enter second number:"))
z= int(input("enter third number:"))
if x < y and x < z :
    print (f'{x} is smallest ')
elif y < x and x < z :
    print(f'(y) is smallest')
else:
    print(f'(z) is smallest')