# Author: Vince Christian Carabanes

import time
import random
from multiprocessing import Pool
from typing import List, Tuple


# STEP 1: Merge two sorted lists into one sorted list
def merge(left: List[int], right: List[int]) -> List[int]:
    merged_result: List[int] = []
    left_index: int = 0
    right_index: int = 0

    # Compare elements from both halves and build sorted result
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged_result.append(left[left_index])
            left_index += 1
        else:
            merged_result.append(right[right_index])
            right_index += 1

    # Append any remaining elements from either half
    merged_result.extend(left[left_index:])
    merged_result.extend(right[right_index:])

    return merged_result


# STEP 2: Recursively split and sort a single chunk
def merge_sort(arr: List[int]) -> List[int]:
    # Base case: a list of 0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr

    midpoint: int = len(arr) // 2
    left_half: List[int] = merge_sort(arr[:midpoint])
    right_half: List[int] = merge_sort(arr[midpoint:])

    return merge(left_half, right_half)


# STEP 3: Worker function called by each process
def sort_chunk(chunk: List[int]) -> List[int]:
    return merge_sort(chunk)


# STEP 4: Combine all sorted chunks into one final list
def merge_all(sorted_chunks: List[List[int]]) -> List[int]:
    # Repeatedly merge pairs of chunks until only one remains
    while len(sorted_chunks) > 1:
        next_level: List[List[int]] = []
        for pair_index in range(0, len(sorted_chunks), 2):
            has_pair = pair_index + 1 < len(sorted_chunks)
            if has_pair:
                merged_pair = merge(sorted_chunks[pair_index], sorted_chunks[pair_index + 1])
                next_level.append(merged_pair)
            else:
                next_level.append(sorted_chunks[pair_index])
        sorted_chunks = next_level

    return sorted_chunks[0]


# MAIN RUNNER: Divide, sort in parallel, then merge
def run_parallel_sort(data: List[int], label: str = "", num_processes: int = 4) -> Tuple[List[int], float]:
    print(f"\n[Parallel Sort] {label}")
    print(f"  Dataset size:    {len(data)}")
    print(f"  Processes used:  {num_processes}")

    chunk_size: int = len(data) // num_processes
    data_chunks: List[List[int]] = [
        data[start:start + chunk_size]
        for start in range(0, len(data), chunk_size)
    ]

    start_time: float = time.time()
    with Pool(processes=num_processes) as process_pool:
        sorted_chunks: List[List[int]] = process_pool.map(sort_chunk, data_chunks)

    fully_sorted: List[int] = merge_all(sorted_chunks)
    end_time: float = time.time()

    elapsed: float = end_time - start_time

    print(f"  First 5 elements: {fully_sorted[:5]}")
    print(f"  Last 5 elements:  {fully_sorted[-5:]}")
    print(f"  Execution time:   {elapsed:.6f} seconds")

    return fully_sorted, elapsed


# ENTRY POINT
if __name__ == "__main__":
    dataset_sizes = {
        "Small (1,000)":        1000,
        "Medium (100,000)":     100_000,
        "Large (1,000,000)":    1_000_000,
    }

    for size_label, total_elements in dataset_sizes.items():
        random_data: List[int] = [random.randint(1, 1_000_000) for _ in range(total_elements)]
        run_parallel_sort(random_data, size_label)

    already_sorted: List[int] = list(range(1, 10_001))
    run_parallel_sort(already_sorted, "Special Case - Already Sorted (10,000)")

    reverse_sorted: List[int] = list(range(10_000, 0, -1))
    run_parallel_sort(reverse_sorted, "Special Case - Reverse Sorted (10,000)")