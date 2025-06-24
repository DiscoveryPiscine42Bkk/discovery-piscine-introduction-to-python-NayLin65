def transform_array():
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]
    new_array = [num + 2 for num in original_array]
    
    unique_new_values = set(new_array)
    
    print(original_array)
    print(unique_new_values)

if __name__ == "__main__":
    transform_array()
