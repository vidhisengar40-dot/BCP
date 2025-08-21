A = int(input("Enter a positive integer: "))
odd_sum = 0
for i in range(1, A + 1, 2):  
    odd_sum += i

print("Sum of odd numbers from 1 to", A, "is:", odd_sum)