A = int(input("Enter the first number (A): "))
B = int(input("Enter the first number (B): "))
C = int(input("Enter the first number (C): "))

if A < B:
    print("Minimum is:", A)
elif B < A:
    print("Minimum is:", B)
elif B < C:
    print("Minimum is:", C)    
else:
    print("Both numbers are equal:", A)
