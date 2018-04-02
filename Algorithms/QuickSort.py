"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    if len(array) <= 1:
        return array
    elif len(array) == 2:
        if array[0] > array[1]:
            return [array[1], array[0]]
        else:
            return array
    else:
        pivot = array[-1]
        pivot_idx = len(array)-1
        idx = 0
        while idx < pivot_idx:
            count = 0
            if array[idx] > pivot:
                array[pivot_idx] = array[idx]
                array[idx] = array[pivot_idx-1]
                array[pivot_idx-1] = pivot
                pivot_idx += -1
                count += 1
            if count == 0:
                idx += 1
        if (pivot_idx + 1 == len(array)):
            return quicksort(array[:-1]) + [pivot]
        elif (pivot_idx == 0):
            return [pivot] + quicksort(array[1:])
        else:
            return quicksort(array[:pivot_idx]) + [pivot] + quicksort(array[pivot_idx+1:])

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)