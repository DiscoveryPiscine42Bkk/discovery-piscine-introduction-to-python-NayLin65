import sys

def display_parameter_count():
    parameter_count = len(sys.argv) - 1  # Subtract 1 to exclude the script name
    print(f"Number of parameters: {parameter_count}.")

if __name__ == "__main__":
    display_parameter_count()
