# Time Complexity: O(n^2)
# Space Complexity: O(1)

arr = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def bubble_sort(arr):
    n = len(arr)
    flag = True

    while flag:
        flag = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                flag = True

    return arr

print(bubble_sort(arr))
