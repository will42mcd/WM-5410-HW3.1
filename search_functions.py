# Code taken from
# https://www.geeksforgeeks.org/binary-search/
# Accessed on 08/22/24
# No atributiuon or license listed
# Python3 code to implement iterative Binary
# Search.


# It returns location of x in given array arr
def binary_search_sub(arr, low, high, x):
    mid = 0
    while low <= high:

        mid = low + (high - low) // 2 

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        else:
            high = mid - 1

    # If we reach here, then the element
    # was not present
    return mid


# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10

    # Function call
    result = binary_search_sub(arr, 0, len(arr)-1, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")
