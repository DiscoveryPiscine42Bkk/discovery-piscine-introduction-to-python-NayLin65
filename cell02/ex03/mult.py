def main():
    try:
        
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
   
        product = num1 * num2
        
        
        if product > 0:
            sign = "The result is positive"
        elif product < 0:
            sign = "The result is negative"
        else:
            sign = "The result is positive and negative"
        

        print(f"The result of the multiplication is {sign}.")
        print(f"Result: {product}")
        
    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()
