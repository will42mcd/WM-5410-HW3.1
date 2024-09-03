# Code taken from:
# https://www.geeksforgeeks.org/selection-sort-algorithm-2/
# Accessed on 08/22/24
# No atributiuon or license listed
# CHANGELOG:
# added a custom compare function support
# Python program for implementation of Selection
# Sort

# This function is same in both iterative and recursive
def partition(arr,l,h):
    i = ( l - 1 )
    x = arr[h]
 
    for j in range(l , h):
        if arr[j] <= x:
 
            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
 
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return (i+1)
 
# Function to do Quick sort
# arr[] --> Array to be sorted,
# l --> Starting index,
# h --> Ending index
def quickSortIterative(arr,l,h,compare):
    
    # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * (size)
 
    # initialize top of stack
    top = -1
 
    # push initial values of l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
 
    # Keep popping from stack while is not empty
    while top >= 0:
 
        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
 
        # Set pivot element at its correct position in
        # sorted array
        p = partition( arr, l, h )
 
        # If there are elements on left side of pivot,
        # then push left side to stack
        if compare(arr[p-1][0][0] , l):
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
 
        # If there are elements on right side of pivot,
        # then push right side to stack
        if compare(arr[p+1][0][0], h):
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h


def selection_sort(A, compare):

    # Traverse through all array elements
    for i in range(len(A)-1):
    
        # Find the minimum element in remaining 
        # unsorted array
        min_idx = i
        for j in range(i+1, len(A)):
            if compare(A[min_idx] , A[j]):
                min_idx = j
            
        # Swap the found minimum element with 
        # the first element        
        A[i], A[min_idx] = A[min_idx], A[i]
# def selection_sort(A)

# perform bottom up merge
def mergeSort(a):
    # start with least partition size of 2^0 = 1
    width = 1   
    n = len(a)                                          
    # subarray size grows by powers of 2 
    # since growth of loop condition is exponential, 
    # time consumed is logarithmic (log2n)
    while (width < n):
        # always start from leftmost
        l=0;
        while (l < n): 
            r = min(l+(width*2-1), n-1)         
            m = min(l+width-1,n-1)
            # final merge should consider 
            # unmerged sublist if input arr
            # size is not power of 2              
            merge(a, l, m, r)
            l += width*2
        # Increasing sub array size by powers of 2
        width *= 2
    return a
   
# Merge Function 
def merge(a, l, m, r): 
    n1 = m - l + 1
    n2 = r - m 
    L = [0] * n1 
    R = [0] * n2 
    for i in range(0, n1): 
        L[i] = a[l + i] 
    for i in range(0, n2): 
        R[i] = a[m + i + 1] 
 
    i, j, k = 0, 0, l 
    while i < n1 and j < n2: 
        if L[i] <= R[j]: 
            a[k] = L[i] 
            i += 1
        else: 
            a[k] = R[j] 
            j += 1
        k += 1
 
    while i < n1: 
        a[k] = L[i] 
        i += 1
        k += 1
 
    while j < n2: 
        a[k] = R[j] 
        j += 1
        k += 1

if __name__ == '__main__':
    A = [64, 25, 12, 22, 11]

    # Driver code to test above
    print ("Sorted array")
    selection_sort(A)
    print(A)
