# # TO-DO: complete the helpe function below to merge 2 sorted arrays
# def merge( arrA, arrB ):
#     print(f"MERGE: {arrA} {arrB}")
#     num_elements = len( arrA ) + len( arrB )
#     merged_arr = [0] * num_elements
#     #
#     # a_index = 0
#     # b_index = 0
#     #
#     # for i in range(0, elements):
#     #
#     #     if a_index >= len(arrA):
#     #         merged_arr[i] = arrB[b_index]
#     #         b_index += 1
#     #     elif b_index >= len(arrB):
#     #         merged_arr[i] = arrA[a_index]
#     #         a_index += 1
#     #     elif arrA[a_index] <= arrB[b_index]:
#     #         merged_arr[i] = arrA[a_index]
#     #         a_index += 1
#     #     elif arrB[b_index] <= arrA[a_index]:
#     #         merged_arr[i] = arrB[b_index]
#     #         b_index += 1
#
#     a_i = 0 # a_i is the current index for array a
#     b_i = 0 # b_i is the current index for array b
#
#     # for each index in the merged array `elements`...
#     for i in range(num_elements):
#         #find the smallest first-item between array A and array B
#         #add that to `elements` at the given index
#         #increment the a/b counter
#         #1. A is empty, B is not empty
#         print(f"MERGE SORT: {arr}")
#         if a_i >= len(arrA):
#             merged_arr[i] = arrB[b_i]
#             b_i += 1
#         #2. B is empty, A is not empty
#         elif b_i >= len(arrB):
#             merged_arr[i] = arrA[a_i]
#             a_i += 1
#         #3. A has the smaller element
#         elif arrA[a_i] <= arrB[b_i]:
#             merged_arr[i] = arrA[a_i]
#             a_i += 1
#         #4. B has the smaller element
#         else:
#             merged_arr[i] = arrB[b_i]
#             b_i += 1
#
#     return merged_arr
#
# TO-DO: implement the Merge Sort function below USING RECURSION
# def merge_sort( arr ):
#     if len(arr) > 1:
#         #split
#         half_point = len(arr) // 2
#         left_arr = arr[:half_point]
#         right_arr = arr[half_point:]
#
#         #split each of the sorted arrays
#         #recursion will keep going through merge_sort calls breaking arr into smaller pieces until base case is hit(len(arr) > 1)
#         left = merge_sort(left_arr)
#         right = merge_sort(right_arr)
#
#         #merge the sorted arrays
#         #this will not happen until the left and right recursions have hit base case
#         arr = merge(left, right)
#     return arr

import random
def merge( arrA, arrB ):
    print(f"MERGE: {arrA} - {arrB}")
    num_elements = len( arrA ) + len( arrB )
    merged_arr = [0] * num_elements
    # 3. Start merging your single lists of one element together into larger, sorted sets
    # 4. Repeat step 3 until the entire data set has been reassembled
    a_i = 0   # a_i is the current index for arrA
    b_i = 0   # b_i is the current index for arrB
    # for each index in the merged array `elements`...
    for i in range(num_elements):
        # Find the smallest first-item between arrA and arrB
        # Add that to `elements` at the given index
        # Increment the a/b counter
        if a_i >= len(arrA):
            # 1. A is empty, B is not empty
            merged_arr[i] = arrB[b_i]
            b_i += 1
        elif b_i >= len(arrB):
            # 2. B is empty, A is not empty
            merged_arr[i] = arrA[a_i]
            a_i += 1
        elif arrA[a_i] < arrB[b_i]:
            # 3. A has the smaller element
            merged_arr[i] = arrA[a_i]
            a_i += 1
        else: # arrA[a_i] >= arrB[b_i]:
            # 4. B has the smaller element
            merged_arr[i] = arrB[b_i]
            b_i += 1
    print(f"  * MERGED - {merged_arr}")
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # 1. While your data set contains more than one item, split it in half
    # 2. Once you have gotten down to a single element, you have also *sorted* that element
    #    (a single element cannot be "out of order")
    print(f"MERGE SORT: {arr}")
    if len(arr) > 1:
        # Split
        midway_point = len(arr) // 2
        left_arr = arr[ : midway_point]
        right_arr = arr[midway_point : ]
        # Sort each of the split arrays
        sorted_left = merge_sort(left_arr)
        sorted_right = merge_sort(right_arr)
        # Merge the sorted arrays
        arr = merge(sorted_left, sorted_right)
    return arr


arr = list(range(20))
random.shuffle(arr)

merge_sort(arr)
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
