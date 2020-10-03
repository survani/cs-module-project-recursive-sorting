# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    merged_arr = []

    # Your code here
    x = 0
    y = 0

    while x < len(arrA) and y < len(arrB):
        if arrA[x] < arrB[y]:
            merged_arr.append(arrA[x])
            x += 1
        else:
            merged_arr.append(arrB[y])
            y += 1

    while x < len(arrA):
        merged_arr.append(arrA[x])
        x += 1
    while y < len(arrB):
        merged_arr.append(arrB[y])
        y += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here

    if len(arr) > 1:
        lft = merge_sort(arr[:len(arr) // 2])
        rght = merge_sort(arr[len(arr) // 2:])
        arr = merge(lft, rght)
    return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass


# Your code here


def merge_sort_in_place(arr, l, r):
    pass
# Your code here
