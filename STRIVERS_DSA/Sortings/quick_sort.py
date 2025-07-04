import random

class Solution:
    @staticmethod
    def quick_sort(arr, low, high):
        # Base case: if the subarray has less than 2 elements, it's sorted
        if low < high:
            # Random pivot selection to avoid worst-case
            pivot_index = random.randint(low, high)
            arr[low], arr[pivot_index] = arr[pivot_index], arr[low]

            # Partition the array and get the pivot position
            pi = Solution.partition(arr, low, high)
            # Recursively sort elements before and after partition
            Solution.quick_sort(arr, low, pi - 1)
            Solution.quick_sort(arr, pi + 1, high)

    @staticmethod
    def partition(arr, low, high):
        # Choose the first element as pivot (after random swap)
        pivot = arr[low]
        i = low + 1
        j = high

        while True:
            # Move i to the right as long as arr[i] <= pivot
            while i <= j and arr[i] <= pivot:
                i += 1
            # Move j to the left as long as arr[j] > pivot
            while i <= j and arr[j] > pivot:
                j -= 1
            # Swap elements at i and j if needed
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break

        # Place the pivot in its correct position
        arr[low], arr[j] = arr[j], arr[low]
        return j


# Input and usage
arr = list(map(int, input("Enter the elements of the array: ").split()))
Solution.quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)