# pdc-activities-cs3b

---

## Lab 2 – Exploring Multithreading and Multiprocessing in Python

### Description
This laboratory activity demonstrates the use of multithreading and multiprocessing in Python to compute the General Weighted Average (GWA). User input is accepted for subject grades, and execution time is measured using the `time` module within each implementation.

### Sample Input Used
The following grades were entered during testing:

- **Multithreading:** 85, 75, 80, 80  
- **Multiprocessing:** 80, 85, 75, 80

### Execution Time Comparison

| Method | Execution Order | GWA Output | Execution Time |
|------|----------------|-----------|----------------|
| Multithreading | Threads execute concurrently and finish in non-deterministic order | Single correct GWA value displayed after all threads complete | ~0.000296 seconds |
| Multiprocessing | Processes execute independently and finish in non-deterministic order | Per-process outputs with final GWA computed by the main process | ~0.002787 seconds |

### Discussion
Outputs may appear in different order because threads and processes are scheduled by the operating system. Since they run concurrently, the execution order depends on which thread or process completes first.

### Optimization
Execution time measurement was integrated directly into both multithreading and multiprocessing implementations to simplify the program structure and improve readability while still allowing accurate performance comparison.

### Guide Questions

1. **Which approach demonstrates true parallelism in Python? Explain.**  
   Multiprocessing demonstrates true parallelism because it uses separate processes that can run on multiple CPU cores.

2. **Compare execution times between multithreading and multiprocessing.**  
   Multithreading executed faster due to lower overhead, while multiprocessing took longer because creating multiple processes requires more system resources.

3. **Can Python handle true parallelism using threads? Why or why not?**  
   No, Python threads cannot achieve true parallelism for CPU-bound tasks due to the Global Interpreter Lock (GIL).

4. **What happens if you input a large number of grades (e.g., 1000)? Which method is faster and why?**  
   With a large number of grades, multiprocessing performs better because tasks can be distributed across multiple CPU cores.

5. **Which method is better for CPU-bound tasks and which for I/O-bound tasks?**  
   Multiprocessing is better for CPU-bound tasks, while multithreading is more suitable for I/O-bound tasks.

6. **How did your group apply creative coding or algorithmic solutions in this lab?**  
   The group integrated execution time measurement directly into each implementation and used structured user input handling to make the programs more efficient and readable.

## Lab 3 Questions

1. **Task vs Data Parallelism**
Task Parallelism means different tasks run at the same time — Part A shows this because each deduction type (SSS, PhilHealth, etc.) is a separate function running concurrently on the same salary. Data Parallelism means the same task runs on different data simultaneously — Part B shows this because one payroll function is applied to all five employees at the same time.

2. **How concurrent.futures manages execution**
submit() schedules a single callable and returns a Future object that holds the result once it’s done. map() is a cleaner way to apply one function across multiple inputs in parallel. Future lets you retrieve results asynchronously using .result(). The with statement is used so the executor automatically shuts down and cleans up threads/processes after the block finishes — no manual cleanup needed.

3. **ThreadPoolExecutor and the GIL**
No, true parallelism didn’t occur. Python’s GIL only allows one thread to execute Python bytecode at a time, so threads take turns rather than truly running side by side. ThreadPoolExecutor works well for I/O-bound tasks, but since deduction calculations are CPU-bound, threads don’t really speed things up — they just run concurrently, not in parallel.

