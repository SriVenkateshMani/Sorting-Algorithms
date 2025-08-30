# Time Complexity: O(nlogn)
# Space Complexity: O(n)

arr = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def merge_sort(arr):
    n = len(arr)

    if n == 1:
        return arr
    
    # Segregating the array to its left and right half

    m = len(arr) // 2
    L = arr[:m]
    R = arr[m:]

    # Performing recursion

    L = merge_sort(L)
    R = merge_sort(R)

    # Merging the smaller portions 

    left_1, left_2 = 0,0
    L_len = len(L)
    R_len = len(R)

    # The final resulting sorted array
    sorted_arr = [0] * n
    i = 0

    while left_1 < L_len and left_2 < R_len:
        if L[left_1] < R[left_2]:
            sorted_arr[i] = L[left_1]
            left_1 += 1
        else:
            sorted_arr[i] = R[left_2] 
            left_2 += 1
        
        i += 1
    
    # Handling the remaining values either on the left or right halves

    while left_1 < L_len:
        sorted_arr[i] = L[left_1]
        left_1 += 1
        i += 1
    
    while left_2 < R_len:
        sorted_arr[i] = R[left_2]
        left_2 += 1
        i += 1
    
    return sorted_arr

print(merge_sort(arr))
