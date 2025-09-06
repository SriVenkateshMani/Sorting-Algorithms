# Time Complexity: O(nlogn)
# Space Complexity: O(n)
# Note: O(1) space is possible via swapping, but this is complex

import heapq

arr = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def heapsort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0] * n

    for i in range(n):
        minn = heapq.heappop(arr)
        new_list[i] = minn
    
    return new_list

print(heapsort(arr))