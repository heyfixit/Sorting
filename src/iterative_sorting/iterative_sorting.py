# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j





        # TO-DO: swap
        holder = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = holder




    return arr

# print(selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    i = 1
    while i <= len(arr) - 1:
        if arr[i - 1] > arr[i]:
            holder = arr[i]
            arr[i] = arr[i - 1]
            arr[i - 1] = holder
            i = 1
        else:
            i += 1

    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
