def check_decimal():
    print("Enter a number:")
    user_input = input().strip()
    
    try:
        num = float(user_input)
        if num.is_integer():
            print("This is an integer")
        else:
            print("This is a decimal")
    except ValueError:
        print(f"'{user_input}' is not a valid number")

if __name__ == "__main__":
    check_decimal()
