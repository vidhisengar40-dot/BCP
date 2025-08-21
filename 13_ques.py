A = int(input("Enter first number (A): "))
B = int(input("Enter second number (B): "))

if A > B:
    print("Maximum is:", A)
elif B > A:
    print("Maximum is:", B)
else:
    print("Both numbers are equal:", A)