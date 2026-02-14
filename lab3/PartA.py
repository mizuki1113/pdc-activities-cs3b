import threading
from concurrent.futures import ThreadPoolExecutor

def compute_sss(salary):
    result = salary * 0.045
    print(f"  [SSS] Thread: {threading.current_thread().name} | Deduction: {result:.2f}")
    return result

def compute_philhealth(salary):
    result = salary * 0.025
    print(f"  [PhilHealth] Thread: {threading.current_thread().name} | Deduction: {result:.2f}")
    return result

def compute_pagibig(salary):
    result = salary * 0.02
    print(f"  [Pag-IBIG] Thread: {threading.current_thread().name} | Deduction: {result:.2f}")
    return result

def compute_tax(salary):
    result = salary * 0.10
    print(f"  [Tax] Thread: {threading.current_thread().name} | Deduction: {result:.2f}")
    return result

def run_task_parallelism():
    salary = 25000  # Using Alice's salary as example
    print(f"\n=== Part A: Task Parallelism (ThreadPoolExecutor) ===")
    print(f"Employee: Alice | Gross Salary: {salary:.2f}\n")

    deduction_functions = [compute_sss, compute_philhealth, compute_pagibig, compute_tax]
    deduction_names = ["SSS", "PhilHealth", "Pag-IBIG", "Withholding Tax"]

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {name: executor.submit(func, salary) 
                   for name, func in zip(deduction_names, deduction_functions)}

    print("\n--- Results ---")
    total_deduction = 0
    for name, future in futures.items():
        amount = future.result()
        print(f"{name}: {amount:.2f}")
        total_deduction += amount

    print(f"\nTotal Deduction: {total_deduction:.2f}")
    print(f"Net Salary:      {salary - total_deduction:.2f}")

run_task_parallelism()