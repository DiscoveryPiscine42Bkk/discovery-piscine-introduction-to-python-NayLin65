try:
    num = float(input("Enter a number: "))
except ValueError:
    print("Error: Please enter a valid number.")
    exit(1)
if num == 0:
    print("This number is equal to zero.")
else:
    print("This number is different from zero.")
