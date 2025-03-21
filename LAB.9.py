print("__________________________________________________")
def count_lower_upper(s):
   
    lower_count = 0
    upper_count = 0
    
    
    for char in s:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
    
    
    return {"lowercase": lower_count, "uppercase": upper_count}


sample_string = "Hello World! Python IS Fun"
result = count_lower_upper(sample_string)
print(result)
print("__________________________________________________")
def compute(n):
    
    n_str = str(n)
    
    result = int(n_str) + int(n_str*2) + int(n_str*3) + int(n_str*4)
    return result


for digit in range(4, 8):
    print(f"Result for n={digit}: {compute(digit)}")

print("__________________________________________________")
import numpy as np

def create_array(depth, rows, cols, initial_value):
    
    array = np.full((depth, rows, cols), initial_value)
    return array

depth = 3
rows = 4
cols = 5
initial_value = 7

array = create_array(depth, rows, cols, initial_value)


print(array)
print("__________________________________________________")


