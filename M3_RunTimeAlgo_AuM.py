#M3 Analyze Running Time of Search Algo's in Python, AuM

from search_algorithms import recursive_binary_search, iterative_binary_search, sequential_search
import random
import time

def runtest_3():
    dataSize = [5000, 50000, 100000, 150000, 1000000]
    results_table=[]

    print("Beginning test:")
    print("-"*40)
    
    for N in dataSize:
        sumRBS = 0
        sumIBS = 0
        sumSS = 0

        for _ in range(10):
            arr=sorted([random.randint(1,1000000) for _ in range(N)])
            target=random.randint(1,1000000)

            #recursive:
            start=time.perf_counter()
            recursive_binary_search(arr, target, 0, len(arr)-1)
            end=time.perf_counter()
            sumRBS+=(end-start)*1_000_000

            #iterative:
            start=time.perf_counter()
            iterative_binary_search(arr, target)
            end=time.perf_counter()
            sumIBS+=(end-start)*1_000_000

            #sequential:
            start=time.perf_counter()
            sequential_search(arr,target)
            end=time.perf_counter()
            sumSS+=(end-start)*1_000_000

        #calc avgs:
        avgr=sumRBS/10
        avgi=sumIBS/10
        avgsq=sumSS/10

        #storage for final table:
        results_table.append((N, avgr, avgi, avgsq))
        
        #print avgs:
        print(f"N = {N}")
        print(f"Average Recursive Binary Search time: {avgr:.2f} μs")
        print(f"Average Iterative Binary Search time: {avgi:.2f} μs")
        print(f"Average Sequential Search time: {avgsq:.2f} μs")

        #final results table + formatting:
        print("\nResults:")
        print(f"{'Size of Data (N)':<20} | {'Recursive BS (μs)':<20} | {'Iterative BS (μs)':<20} | {'Sequential BS (μs)':>20}")
        print("-"*90)
        for row in results_table:
            print(f"{row[0]:<20} | {row[1]:<20.2f} | {row[2]:<20.2f} | {row[3]:<20.2f}")

        print("\nEnd of Results")
if __name__ == "__main__":
    runtest_3()