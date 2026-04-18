import time
import random


def merge(l, r):
    res, i, j = [], 0, 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            res.append(l[i]); i += 1
        else:
            res.append(r[j]); j += 1
    return res + l[i:] + r[j:]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


def run_sequential_sort(data, label=""):
    print("\nSequential Sort:", label)
    print("Dataset size:", len(data))

    t0 = time.time()
    sorted_data = merge_sort(data)
    elapsed = time.time() - t0

    print("First 5 elements:", sorted_data[:5])
    print("Last 5 elements:",  sorted_data[-5:])
    print(f"Execution time: {elapsed:.6f} seconds")

    return sorted_data, elapsed


if __name__ == "__main__":
    cases = {
        "1,000":     1000,
        "100,000":  100_000,
        "1,000,000": 1_000_000,
    }

    for label, n in cases.items():
        run_sequential_sort([random.randint(1, 1_000_000) for _ in range(n)], label)

    run_sequential_sort(list(range(1, 10_001)),    "Special Case - Already Sorted (10,000)")
    run_sequential_sort(list(range(10_000, 0, -1)), "Special Case - Reverse Sorted (10,000)")