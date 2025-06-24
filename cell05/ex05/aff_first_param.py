import sys

def display_first_param():
    if len(sys.argv) < 2:  
        print("none")
    else:
        print(sys.argv[1])  

if __name__ == "__main__":
    display_first_param()
