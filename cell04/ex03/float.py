def check_decimal():
    print("Enter a number:")
    user_input = input().strip()
    
    try:
        num = float(user_input)
        if num.is_integer():
            print(f"{user_input} is not a decimal (it's a whole number)")
        else:
            print(f"{user_input} is a decimal")
    except ValueError:
        print(f"'{user_input}' is not a valid number")

if __name__ == "__main__":
    check_decimal()
