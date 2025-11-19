#M3 Analyze Running Time of Search Algo's in Python, AuM

from search_algorithms import recursive_binary_search, iterative_binary_search, sequential_search
import random

def runtest_1():
    arr = [3, 5, 8, 12, 14, 18, 21]
    arr.sort()
    target1 = 12 # Present
    target2 = 9  # Not present
    
    # Recursive Binary Search
    index = recursive_binary_search(arr, target1, 0, len(arr) - 1)
    print(f"Recursive: {target1} found at index {index}" if index != -1 else f"Recursive: {target1} not found")
    index = recursive_binary_search(arr, target2, 0, len(arr) - 1)
    print(f"Recursive: {target2} found at index {index}" if index != -1 else f"Recursive: {target2} not found")

    # Iterative Binary Search
    index = iterative_binary_search(arr, target1)
    print(f"Iterative: {target1} found at index {index}" if index != -1 else f"Iterative: {target1} not found")
    index = iterative_binary_search(arr, target2)
    print(f"Iterative: {target2} found at index {index}" if index != -1 else f"Iterative: {target2} not found")

    # Sequential Search
    index = sequential_search(arr, target1)
    print(f"Sequential: {target1} found at index {index}" if index != -1 else f"Sequential: {target1} not found")
    index = sequential_search(arr, target2)
    print(f"Sequential: {target2} found at index {index}" if index != -1 else f"Sequential: {target2} not found")

if __name__ == "__main__":
    runtest_1()