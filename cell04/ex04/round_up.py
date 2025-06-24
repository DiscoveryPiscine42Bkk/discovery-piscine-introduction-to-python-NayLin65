def round_up_number():
    print("Enter a number:")
    try:
        number = float(input())
        rounded = math.ceil(number)
        print(f"Rounded up: {rounded}")
    except ValueError:
        print("Please enter a valid number")
