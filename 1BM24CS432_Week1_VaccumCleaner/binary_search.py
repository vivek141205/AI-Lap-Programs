def binary_search(arr:list[int], target:int)->int:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1
        
        else:
            high = mid - 1

    return -1

arr = [1,2,3,4,5,6,7,8]
target = int(input("plese enter a target : "))

result_index = binary_search(arr, target)

print(result_index)
