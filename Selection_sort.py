# Time Complexity: O(n^2)
# Space Complexity: O(1)

arr = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

print(selection_sort(arr))