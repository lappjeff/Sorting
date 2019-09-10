array = [5, 1, 8, 3, 4]

def selection_sort(arr):
    #no need to check the last element because it will be the right value by the time it gets there\
    for i in range(0, len(arr) - 1):

        #current for loop index
        cur_index = i
        #index of the smallest value
        smallest_index = cur_index

        #checks everything from current index on to skip sorted list items on left
        for j in range(cur_index, len(arr)):
            print(f"Is {arr[j]} less than {arr[smallest_index]}?")
            #check if value at j is smaller than value at smallest_index
            if arr[j] < arr[smallest_index]:
                #if it is, set the j index as the new smallest_index
                smallest_index = j

        #after exiting if statement, stores the value at smallest_index into temp var
        temp = arr[smallest_index]


        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr
print(selection_sort(array))

# TO-DO:  implement the Bubble Sort function below



def bubble_sort( arr ):
    swap_occured = True

    while swap_occured:
        swap_occured = False
        for index in range(0, len(arr) - 1):
            # index is left hand value
            #j is right hand value
            j = index + 1

            #temp holds the value of j to switch with i in if statement
            temp = arr[j]

            if arr[index] > arr[j]:
                arr[j] = arr[index]
                arr[index] = temp
                swap_occured = True

    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
