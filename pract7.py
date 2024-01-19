# Python3 program to find first
# non-repeating element.
 
 
def firstNonRepeating(arr, n):
 
    # Loop for checking each element
    for i in range(n):
        j = 0
        # Checking if ith element is present in array
        while(j < n):
            if (i != j and arr[i] == arr[j]):
                break
            j += 1
        # if ith element is not present in array
        # except at ith index then return element
        if (j == n):
            return arr[i]
 
    return -1
 
 
# Driver code
arr = [5, 4, 5, 6, 7, 4]
n = len(arr)
print(firstNonRepeating(arr, n))