def bubble_sort(arr:list[int])->list[int]:
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = [2,5,4,7,8,5,6]

print(bubble_sort(arr))