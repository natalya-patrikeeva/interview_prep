"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quicksort(array):

    if len(array) >= 2:
        low = 0
        pivot = len(array) - 1

        while (low < pivot):

            if array[low] < array[pivot]:
                low += 1

            else:
                tmp = array[low]
                array[low] = array[pivot - 1]
                array[pivot - 1] = array[pivot]
                array[pivot] = tmp
                pivot -= 1

        array = quicksort(array[:pivot]) + [array[pivot]] + quicksort(array[pivot + 1 :] )
        return array

    else:
        return array



test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print test
print quicksort(test)
