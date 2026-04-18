# Author: Keissha Louise Canios

import time
import random

# Search Logic

find_index = lambda data, target: next(
    (i for i, val in enumerate(data) if val == target), -1
)

make_dataset = lambda n: [random.randint(1, 1_000_000) for _ in range(n)]

def run_sequential_search(data, target, label=""):
    print(f"\n[Sequential Search] {label}")
    print(f"  Dataset size: {len(data)}")
    print(f"  Target value: {target}")

    start = time.time()
    result = find_index(data, target)
    elapsed = time.time() - start

    print(f"  Found at index: {result}" if result != -1 else "  Target not found in dataset.")
    print(f"  Execution time: {elapsed:.6f} seconds")

    return result, elapsed

# Dataset Configurations

SIZES = {
    "Small (1,000)":        1000,
    "Medium (100,000)":     100_000,
    "Large (1,000,000)":    1_000_000,
}

SPECIAL_CASES = [
    (list(range(1, 10_001)),      7500,  "Already Sorted (10,000) - Target Exists"),
    (list(range(1, 10_001)),      99999, "Already Sorted (10,000) - Target Missing"),
    (list(range(10_000, 0, -1)),  250,   "Reverse Sorted (10,000) - Target Exists"),
    (list(range(10_000, 0, -1)),  0,     "Reverse Sorted (10,000) - Target Missing"),
]

# Entry Point

if __name__ == "__main__":
    random_runs = [
        (make_dataset(n), label, n)
        for label, n in SIZES.items()
    ]

    for data, label, n in random_runs:
        run_sequential_search(data, data[n // 2], f"{label} - Target Exists")
        run_sequential_search(data, -1,            f"{label} - Target Missing")

    for data, target, label in SPECIAL_CASES:
        run_sequential_search(data, target, label)