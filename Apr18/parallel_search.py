# parallel_search.py
# Author: Precious B. Gamalo

import time
import random
from multiprocessing import Process, Queue


class ParallelSearcher:
    def __init__(self, num_processes=4):
        self.num_processes = num_processes
        self.queue = Queue()

    def _worker(self, sub_data, target, offset):
        for i in range(len(sub_data)):
            if sub_data[i] == target:
                self.queue.put(offset + i)
                return
        self.queue.put(-1)

    def _split_data(self, data):
        chunk_size = len(data) // self.num_processes
        chunks = []
        offsets = []
        for i in range(0, len(data), chunk_size):
            chunks.append(data[i:i + chunk_size])
            offsets.append(i)
        return chunks, offsets

    def _collect_results(self):
        results = []
        while not self.queue.empty():
            results.append(self.queue.get())
        found = [r for r in results if r != -1]
        return min(found) if found else -1

    def search(self, data, target, label=""):
        print(f"\n[Parallel Search] {label}")
        print(f"  Dataset size:   {len(data)}")
        print(f"  Target value:   {target}")
        print(f"  Processes used: {self.num_processes}")

        chunks, offsets = self._split_data(data)
        processes = []

        start = time.time()
        for i in range(len(chunks)):
            p = Process(target=self._worker, args=(chunks[i], target, offsets[i]))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()
        end = time.time()

        final_result = self._collect_results()
        elapsed = end - start

        if final_result != -1:
            print(f"  Found at index: {final_result}")
        else:
            print(f"  Target not found in dataset.")
        print(f"  Execution time: {elapsed:.6f} seconds")

        return final_result, elapsed


class DatasetRunner:
    SIZES = {
        "Small (1,000)": 1000,
        "Medium (100,000)": 100_000,
        "Large (1,000,000)": 1_000_000,
    }

    def __init__(self):
        self.searcher = ParallelSearcher()

    def run_all(self):
        for label, n in self.SIZES.items():
            data = [random.randint(1, 1_000_000) for _ in range(n)]
            self.searcher.search(data, data[n // 2], f"{label} - Target Exists")
            self.searcher.search(data, -1, f"{label} - Target Missing")

        sorted_data = list(range(1, 10_001))
        self.searcher.search(sorted_data, 7500, "Already Sorted (10,000) - Target Exists")
        self.searcher.search(sorted_data, 99999, "Already Sorted (10,000) - Target Missing")

        reverse_data = list(range(10_000, 0, -1))
        self.searcher.search(reverse_data, 250, "Reverse Sorted (10,000) - Target Exists")
        self.searcher.search(reverse_data, 0, "Reverse Sorted (10,000) - Target Missing")


if __name__ == "__main__":
    runner = DatasetRunner()
    runner.run_all()