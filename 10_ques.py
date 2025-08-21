day_number = int(input("Enter a number (1-7): "))

# List of days where index 0 is Sunday
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Check if the input is valid
if 1 <= day_number <= 7:
    print("The day is:", days[day_number - 1])
else:
    print("Invalid input! Please enter a number between 1 and 7.")