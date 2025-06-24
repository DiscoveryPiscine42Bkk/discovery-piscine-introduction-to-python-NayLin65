def transform_array():
    
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]
     
    new_array = []
    for num in original_array:
        if num > 5:
            new_array.append(num + 2)
        else:
            new_array.append(num)
    print("Original array:", original_array)
    print("New array:", new_array)

if __name__ == "__main__":
    transform_array()
