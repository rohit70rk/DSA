# Python code to find duplicates in an array
# using hashmap

def findDuplicates(arr):
  
    # Step 1: Create an empty dictionary
    # to store element frequencies
    freqMap = {}
    result = []

    # Step 2: Iterate through the array and
    # count element frequencies
    for num in arr:
        freqMap[num] = freqMap.get(num, 0) + 1

    # Step 3: Iterate through the dictionary to
    # find duplicates
    for key, value in freqMap.items():
        if value > 1:
            result.append(key)

    # Step 4: If no duplicates found, add -1 to the result
    if not result:
        result.append(-1)

    # Step 6: Return the result list containing
    # duplicate elements or -1
    return result


if __name__ == "__main__":
    arr = [1, 6, 5, 2, 3, 3, 2]
    duplicates = findDuplicates(arr)

    for element in duplicates:
        print(element, end=" ")