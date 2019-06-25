# STRETCH: implement Linear Search
def linear_search(arr, target):
  for i in range(0, len(arr)):
    if arr[i] == target:
      return i

  # TO-DO: add missing code

  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty

  low = 0
  high = len(arr)-1

  # TO-DO: add missing code
  while(high - low > -1):
    mid = low + (high - low) // 2
    if arr[mid] == target:
      return mid

    if high - low == 1 or high == low:
      # we were down to the last element, if it's not here
      # return -1
      if arr[high] != target:
        break
      else:
        return high
    elif target > arr[mid]:
      low = mid
    else:
      high = mid


  return -1 # not found

# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls

  if target == arr[middle]:
    return middle

  if target > arr[middle]:
    return binary_search_recursive(arr[middle:], target, middle, high)
  else:
    return binary_search_recursive(arr[:middle], target, low, middle)
