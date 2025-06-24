def calculate_future_ages():
    print("Enter your current age:")
    try:
        age = int(input())
        if age < 0:
            print("Age cannot be negative!")
            return
        
        print(f"In 10 years, you will be {age + 10} years old.")
        print(f"In 20 years, you will be {age + 20} years old.")
        print(f"In 30 years, you will be {age + 30} years old.")
    except ValueError:
        print("Please enter a valid whole number for your age.")
