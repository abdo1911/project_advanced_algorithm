import time
time_start = time.perf_counter()
from itertools import combinations

def subsetSum(li, comb, sums):
    for i in range(len(li) + 1):
        for subset in combinations(li, i):
            comb.append(list(subset))
            sums.append(sum(subset))

def calcSubsets(n, arr, x):

    arr1, arr2 = arr[:n // 2], arr[n // 2:]
    comb1, sums1 = [], []
    subsetSum(arr1, comb1, sums1)
    comb2, sums2 = [], []
    subsetSum(arr2, comb2, sums2)
    for i in range(len(sums1)):
        for j in range(len(sums2)):
            if sums1[i] + sums2[j] == x:
                print(comb1[i] + comb2[j])

n = 6
arr = [10, 20, 25, 50, 70, 90]
x = 80
calcSubsets(n, arr, x)

time_elapsed = (time.perf_counter() - time_start)

print(time_elapsed)