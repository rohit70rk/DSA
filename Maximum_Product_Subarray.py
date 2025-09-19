def maxProduct(arr):
    n = len(arr)
  
    # Initializing result
    maxProd = arr[0]

    for i in range(n):
        mul = 1
      
        # traversing in current subarray
        for j in range(i, n):
            mul *= arr[j]
          
            # updating result every time
            # to keep track of the maximum product
            maxProd = max(maxProd, mul)
    
    return maxProd

if __name__ == "__main__":
    
    arr = [-2, 6, -3, -10, 0, 2]
    
    print(maxProduct(arr))