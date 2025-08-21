A = int(input("Enter a positive integer: "))
even_sum = 0
for i in range(2, A + 1, 2):   
    even_sum += i

print("Sum of even numbers from 1 to", A, "is:", even_sum)