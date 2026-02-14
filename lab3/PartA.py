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
