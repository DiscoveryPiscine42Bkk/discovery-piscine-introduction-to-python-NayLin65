def simple_calculator():
    print("Give me the first number: ", end="")
    num1 = int(input())
    
    print("Give me the second number: ", end="")
    num2 = int(input())
    
  
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    
   
    try:
        division = num1 // num2
        division_result = f"{division:}"  
    except ZeroDivisionError:
        division_result = "undefined (cannot divide by zero)"
    
  
    print(f"\nResults:")
    print(f"{num1} + {num2} = {addition}")
    print(f"{num1} - {num2} = {subtraction}")
    print(f"{num1} × {num2} = {multiplication}")
    print(f"{num1} ÷ {num2} = {division_result}")
if __name__ == "__main__":
    simple_calculator()
