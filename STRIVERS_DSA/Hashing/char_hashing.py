class Solution:
    @staticmethod
    def char_hashing(arr):
        # Initialize a list of size 256 to store frequency of each character (ASCII)
        hash_array = [0] * 256
        for ch in arr:
            hash_array[ord(ch)] += 1  # Increment the count for the ASCII value of the character
        return hash_array

# Take user input for the size of the array
n = int(input("enter the size of the array: "))
# Take user input for the characters and split into a list
arr = list(input("enter characters: ").split())

# Check if the number of characters matches the specified size
if len(arr) != n:
    print(f"Error: You entered {len(arr)} characters, but expected {n}.")
    exit(1)

# Get the hash array using the static method
hash_array = Solution.char_hashing(arr)

# Take user input for the number of queries
q = int(input("Enter number of queries: "))
for i in range(q):
    ch = input(f"char[{i}]:")
    # Print the frequency of the queried character
    print(hash_array[ord(ch)])