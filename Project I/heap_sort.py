# Hameed Abdul
# 2/22
# Building a Zero index array in python :D
import numpy as np

# Single Dimension 1x8 array Randomly generate by NumPy
arr = np.random.randint(256, size=8)


# Functions to return nodes within a (sub)heap
# Zero based index!!
def left(i):
    return (2 * i) + 1


def right(i):
    return (2 * i) + 2


def parent(i): return (i / 2) - 1


# Use to enforce heap prop
def heapify(arr, i, heap_size):
    '''
    Input an array, parent node index and size of heap to recursively enforces heap properties.
    :return: Proper (sub)heap
    '''

    largest = i
    l = left(i)
    r = right(i)
    # Make comparisons with children
    if l < heap_size and arr[i] < arr[l]:
        largest = l
    else:
        largest = i
    if r < heap_size and arr[largest] < arr[r]:
        largest = r
    # Based on Comparisons,
    # Switch values and Recursively enforce heap prop
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest, heap_size)


# Use to arrange and ensure heap prop on entire array
def build_heap(arr):
    '''
    Iterates through each (sub)heap and enforces props through calling the heapify method
    :param arr: input array
    :param heapsize: current size of heap
    :return: An array that has the props of a heap
    '''

    length = len(arr)
    n = len(arr)
    last_parent = length / 2
    for k in range( (length // 2) - 1, -1, -1):
        heapify(arr, k, n)


# Use to Sort Max Heap Array
def heap_sort(arr):
    """
    Builds the heap, enforces heap prop and decrements heap size to return a sorted array
:param arr: input array
:return: A sorted Heap Array
"""
    # Build a heap array
    build_heap(arr)
    heap_size = len(arr)-1
    # Touch every child and (sub)heap and sort the values
    # Swap first and last value. Reheapify and switch values
    for i in range(len(arr)-1, -1, -1):
        arr[0], arr[heap_size] = arr[heap_size], arr[0]
        heapify(arr, 0, heap_size)
        heap_size -= 1
    return arr

# Use to Test Algorithm


def test_cases():
    t_arr1 = []
    t_arr2 = [3]
    t_arr3 = [3, 0]
    t_arr4 = [3, 0, 1, 10, 18, 4, 7, 20, 10, 15, 9, 2, 12, 14, 5]

    print ("Test Case: ",t_arr1,"\n", heap_sort(t_arr1))
    print ("Test Case: ", t_arr2, "\n", heap_sort(t_arr2))

    print ("Test Case: ",t_arr3)
    print (heap_sort(t_arr3))

    print ("Test Case: ",t_arr4)
    print (heap_sort(t_arr4))

# print ("Random Array : ", arr)
# print ( heap_sort(arr), "\n\n")
# print ("Time to Test \n", "==================================")
# test_cases()
