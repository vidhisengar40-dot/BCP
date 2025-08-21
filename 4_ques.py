def check_last_digit(num):
    return num % 10 == 5

# Test the function
num = int(input("Enter a number: "))
if check_last_digit(num):
    print("The last digit is 5")
else:
    print("The last digit is not 5")