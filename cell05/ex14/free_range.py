import sys

def generate_range():
    if len(sys.argv) != 3:  # Check for exactly 2 parameters (plus script name)
        print("none")
        return
    
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        numbers = list(range(start, end + 1))  # +1 to include the end number
        print(numbers)
    except ValueError:
        print("none")

if __name__ == "__main__":
    generate_range()
