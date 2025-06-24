def round_up_number():
    print("Enter a number:")
    try:
        number = float(input())
        rounded = math.ceil(number)
        print(f"Rounded up: {rounded}")
    except ValueError:
        print("Please enter a valid number")

if __name__ == "__main__":
    round_up_number()
