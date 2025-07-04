# Sorting Algorithms in Python

This folder contains Python implementations of classic sorting algorithms. Each file demonstrates a different sorting technique, with clear comments and explanations. Below is an overview of each algorithm, a description, and an example of how it works, including a step-by-step explanation for each example.

**Note:** In all examples, `n` refers to the number of elements in the array to be sorted.

## 1. Bubble Sort (`bubble_sort.py`)
- **Description:**
  - Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The process is repeated until the list is sorted.
- **Example:**
  - Input: `[5, 2, 9, 1]`
  - Step 1: Compare 5 and 2, swap → `[2, 5, 9, 1]`
  - Step 2: Compare 5 and 9, no swap → `[2, 5, 9, 1]`
  - Step 3: Compare 9 and 1, swap → `[2, 5, 1, 9]`
  - Next pass: Compare 2 and 5, no swap → `[2, 5, 1, 9]`
  - Compare 5 and 1, swap → `[2, 1, 5, 9]`
  - Next pass: Compare 2 and 1, swap → `[1, 2, 5, 9]`
  - Output: `[1, 2, 5, 9]`
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Key Points:**
  - Simple, but inefficient for large datasets.
  - In-place sorting (no extra space needed).

## 2. Insertion Sort (`insertion_sort.py`)
- **Description:**
  - Builds the sorted array one element at a time by repeatedly picking the next element and inserting it into its correct position among the already sorted elements.
- **Example:**
  - Input: `[4, 3, 2, 10, 12, 1, 5, 6]`
  - Step 1: 3 is inserted before 4 → `[3, 4, 2, 10, 12, 1, 5, 6]`
  - Step 2: 2 is inserted before 3 → `[2, 3, 4, 10, 12, 1, 5, 6]`
  - Step 3: 10 stays → `[2, 3, 4, 10, 12, 1, 5, 6]`
  - Step 4: 12 stays → `[2, 3, 4, 10, 12, 1, 5, 6]`
  - Step 5: 1 is inserted at the start → `[1, 2, 3, 4, 10, 12, 5, 6]`
  - Step 6: 5 is inserted before 10 → `[1, 2, 3, 4, 5, 10, 12, 6]`
  - Step 7: 6 is inserted before 10 → `[1, 2, 3, 4, 5, 6, 10, 12]`
  - Output: `[1, 2, 3, 4, 5, 6, 10, 12]`
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Key Points:**
  - Efficient for small or nearly sorted datasets.
  - In-place sorting.

## 3. Selection Sort (`selection_sort.py`)
- **Description:**
  - Divides the array into a sorted and unsorted part, repeatedly selects the minimum element from the unsorted part, and moves it to the end of the sorted part.
- **Example:**
  - Input: `[64, 25, 12, 22, 11]`
  - Step 1: Find min (11), swap with 64 → `[11, 25, 12, 22, 64]`
  - Step 2: Find min (12), swap with 25 → `[11, 12, 25, 22, 64]`
  - Step 3: Find min (22), swap with 25 → `[11, 12, 22, 25, 64]`
  - Step 4: Already sorted → `[11, 12, 22, 25, 64]`
  - Output: `[11, 12, 22, 25, 64]`
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Key Points:**
  - Simple, but not stable.
  - In-place sorting.

## 4. Merge Sort (`merge_sort.py`)
- **Description:**
  - A divide-and-conquer algorithm that splits the array into halves, recursively sorts each half, and then merges the sorted halves.
- **Example:**
  - Input: `[38, 27, 43, 3, 9, 82, 10]`
  - Split: `[38, 27, 43]` and `[3, 9, 82, 10]`
  - Recursively sort: `[27, 38, 43]` and `[3, 9, 10, 82]`
  - Merge: `[3, 9, 10, 27, 38, 43, 82]`
  - Output: `[3, 9, 10, 27, 38, 43, 82]`
- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)
- **Key Points:**
  - Stable and efficient for large datasets.
  - Not in-place (requires extra space for merging).

## 5. Quick Sort (`quick_sort.py`)
- **Description:**
  - A divide-and-conquer algorithm that selects a pivot, partitions the array around the pivot, and recursively sorts the partitions. Uses random pivot selection to avoid worst-case scenarios.
- **Example:**
  - Input: `[10, 7, 8, 9, 1, 5]`
  - Choose pivot (e.g., 7), partition: `[1, 5] [7] [10, 8, 9]`
  - Recursively sort left and right: `[1, 5]` and `[8, 9, 10]`
  - Merge: `[1, 5, 7, 8, 9, 10]`
  - Output: `[1, 5, 7, 8, 9, 10]`
- **Time Complexity:** O(n log n) on average, O(n²) in the worst case
- **Space Complexity:** O(log n) on average, O(n) in the worst case
- **Key Points:**
  - Very efficient for large datasets.
  - In-place sorting, but not stable.

## 6. Recursive Bubble Sort (`recursive_bubble.py`)
- **Description:**
  - A recursive version of bubble sort, where the largest element is moved to the end in each recursive call.
- **Example:**
  - Input: `[3, 2, 1]`
  - First call: swap 3 and 2 → `[2, 3, 1]`, swap 3 and 1 → `[2, 1, 3]`
  - Next call: swap 2 and 1 → `[1, 2, 3]`
  - Output: `[1, 2, 3]`
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Key Points:**
  - Demonstrates recursion with sorting.

## 7. Recursive Insertion Sort (`recursive_insertion.py`)
- **Description:**
  - A recursive version of insertion sort, where the array is sorted up to the (n-1)th element, and the nth element is inserted in the correct position.
- **Example:**
  - Input: `[9, 3, 1, 5, 13, 12]`
  - Recursively sort first 5: `[1, 3, 5, 9, 13]`, insert 12 in correct position → `[1, 3, 5, 9, 12, 13]`
  - Output: `[1, 3, 5, 9, 12, 13]`
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Key Points:**
  - Demonstrates recursion with sorting.

---

Each file is self-contained and can be run directly. Input is taken from the user, and the sorted array is printed as output. Comments in each file explain the logic and steps in detail.

Feel free to explore each file for more details and experiment with different inputs!
