try:
    num = float(input("Enter a number: "))
except ValueError:
    print("Error: Please enter a valid number.")
    exit(1)
if num < 0:
    print("This number is negative.")
elif num > 0:
    print("This number is positive.")
else:
    print("This number is both positive and negative.")
