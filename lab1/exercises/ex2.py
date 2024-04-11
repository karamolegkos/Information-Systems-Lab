"""
Description: Function that returns the sum of the values of a Dictionary.
  -  Input: A Dictionary with numbers as values
  -  Output: The sum of the values
"""
def count_dict(key_values):
    sum = 0
    for key in key_values:
        sum += key_values[key]
    return sum

"""
Description: Function that prints the average of the 
             values of a Dictionary in the first value of a List.
  -  Input: A list with, a Dictionary with numbers as values, in the first value.
  -  Output: No Output
"""
def avg_list(a_list):
    dict_x = a_list[0]
    # print(len(dict_x))    # Prints the amount of keys
    print(count_dict(dict_x) / len(dict_x))

# Initializing the Dictionary
my_dict = {"a": 10, "b":20, "c":30 }

# Printing the sum
print(count_dict(my_dict))

# Creating a list with one value (the Dictionary)
my_list = [my_dict]

# Printing AVG of the values
avg_list(my_list)