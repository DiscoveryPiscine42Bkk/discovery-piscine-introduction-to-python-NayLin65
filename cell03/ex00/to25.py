def main():
    try:
       
        num = int(input("Enter a number: "))
        
 
        if num > 25:
            print("Error")
        else:
         
            for i in range(num, 26): 
                print(i)
    
    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    main()
