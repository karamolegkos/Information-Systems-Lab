"""
Description: Function that it is using call by Reference to extend a List.
  -  Inputs:
    -  list_1: List to be extended
    -  list_2: List that contains the values to extend to the other List
  -  Output: No Output
"""
def extendList(list_1, list_2):
    # Changing list_1 will change it in the caller as well (call by reference)
    list_1.extend(list_2)

"""
Description: Function that returns the sum of the values of a List.
  -  Input: A List with numbers as values
  -  Output: The sum of the values
"""
def sum_list(numbers):
    # Simple sum algorithm
    sum = 0
    for number in numbers:
        sum += number
    return sum

"""
Description: Function that prints the max & min values from a List.
  -  Input: A List with numbers as values
  -  Output: No Output
"""
def max_min_item(numbers):
    # Simple max / min algorithm
    min = numbers[0]
    max = numbers[0]
    
    # for i in range(10):             # From 0 up to 9
    # for i in range(1, 10):          # From 1 up to 9
    for i in range(1, len(numbers)):  # From 1 up to (len(numbers) - 1)
        if min > numbers[i]:
            min = numbers[i]
        if max < numbers[i]:
            max = numbers[i]
    
    print(max, min)

# Initializing Lists
my_list = [100, 200, 300, 199, 99, 9]
a_list = [101, 202, 303]

# Extend the First List with the values of the Second List
extendList(my_list, a_list)

# Print the final List
print(my_list)

# Find the sum of the List and print it
print(sum_list(my_list))

# Find the max and min values of the List
max_min_item(my_list)