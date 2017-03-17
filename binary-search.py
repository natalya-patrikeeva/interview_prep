"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    count = 0
    while len(input_array) > 1:
        array = input_array
        length = len(input_array)

        # Even number of elements
        if length % 2 == 0:
            half_index = length / 2

            if value > input_array[half_index - 1]:
                input_array = input_array[half_index:]
                count += half_index

            elif value < input_array[half_index - 1]:
                input_array = input_array[:half_index]

            else:
                count += half_index - 1
                return count

        # Odd number of elements
        else:
            half_index = (length - 1 ) / 2
            if value > input_array[half_index]:
                input_array = input_array[half_index + 1:]
                count += half_index + 1

            elif value < input_array[half_index]:
                input_array = input_array[:half_index]

            else:
                count += half_index
                return count

    if value == input_array[0]:
         return count
    else:
        return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
