#M3 Analyze Running Time of Search Algo's in Python, AuM

from search_algorithms import recursive_binary_search, iterative_binary_search, sequential_search
import random

def runtest_2():
    arr = [random.randint(1,1000) for _ in range(20)]
    arr.sort()
    print(f"Sorted list: {arr}\n")
    if random.random()<0.5:
        target = random.choice(arr)
    else:
        target = 999
    print(f"Target: {target}")


    print("Test 2:")
    idxr = recursive_binary_search(arr, target, 0, len(arr)-1)
    print(f"Recursive: {'Found' if idxr!=-1 else 'Not Found'}")

    idxi = iterative_binary_search(arr, target)
    print(f"Iterative: {'Found' if idxi!=-1 else 'Not Found'}")

    idxs = sequential_search(arr, target)
    print(f"Sequential: {'Found' if idxs!=-1 else 'Not Found'}")

if __name__ == "__main__":
    runtest_2()