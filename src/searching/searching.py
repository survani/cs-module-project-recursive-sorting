# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here

    # Base Case
    if end >= start:
        midpoint = (end + start) // 2

        # if the target we want to locate is already at the midpoint then simply return the midpoint element.
        if arr[midpoint] == target:
            return midpoint

        # if the target is smaller than the mid go left (-1) of the new subarr
        elif arr[midpoint] > target:
            return binary_search(arr, target, start, midpoint - 1)

        # if the target is greater than the mid go right (+1) of the new subarr
        else:
            return binary_search(arr, target, midpoint + 1, end)
    else:
        # because of how the test want it we have to return - 1 to satisfy the target we chose as not being there.
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
# Your code here
