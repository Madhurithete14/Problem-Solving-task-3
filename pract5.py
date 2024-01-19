#Find nos of mangoes in a bag with maximum mangoes and bag with minimum mangoes given to a student is minimum
 
# Function to check if mid number
def check(n, m, x, y, vl):
     
    # Store the coins
    temp = m
 
    
    if (vl > n):
        return False
 
    
    ex = n - vl
 
    
    ex *= y
 
    # Increment coins by ex
    temp += ex
 
    # Number of mangoes that can be buyed
    # if only x coins needed for one mango
    cr = temp // x
 
    # If the condition is satisfied,
    # return true
    if (cr >= vl):
        return True
 
    # Otherwise return false
    return False
 
# Function to find the maximum number of mangoes

def maximizeMangoes(n, m, x, y):
     
    # Initialize the boundary values
    l = 0
    r = n
 
    # Store the required result
    ans = 0
 
    # Binary Search
    while (l <= r):
 
        # Store the mid value
        mid = l + (r - l) // 2
 
        # Check if it is possible to
        # buy mid number of mangoes
        if (check(n, m, x, y, mid)):
            ans = mid
            l = mid + 1
 
        # Otherwise, update r to mid -1
        else:
            r = mid - 1
 
    # Return the result
    return ans
 
# Driver Code
if __name__ == '__main__':
     
    # Given Input
    W = 4
    C = 8
    x = 4
    y = 4
 
    # Function Call
    print(maximizeMangoes(W, C, x, y))