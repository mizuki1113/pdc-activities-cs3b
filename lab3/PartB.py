from concurrent.futures import ThreadPoolExecutor

employees = [
    ("Alice", 25000),
    ("Bob", 32000),
    ("Charlie", 28000),
    ("Diana", 40000),
    ("Edward", 35000)
]

def compute_payroll(employee):
    name, salary = employee

    sss = salary * 0.045
    philhealth = salary * 0.025
    pagibig = salary * 0.02
    tax = salary * 0.10

    total_deduction = sss + philhealth + pagibig + tax
    net_salary = salary - total_deduction

    return {
        "name": name,
        "gross": salary,
        "sss": sss,
        "philhealth": philhealth,
        "pagibig": pagibig,
        "tax": tax,
        "total_deduction": total_deduction,
        "net_salary": net_salary
    }

def run_data_parallelism():
    print("\n=== Part B: Data Parallelism ===\n")

    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(compute_payroll, employees))

    for r in results:
        print(f"--- {r['name']} ---")
        print(f"  Gross Salary:      {r['gross']:.2f}")
        print(f"  SSS:               {r['sss']:.2f}")
        print(f"  PhilHealth:        {r['philhealth']:.2f}")
        print(f"  Pag-IBIG:          {r['pagibig']:.2f}")
        print(f"  Withholding Tax:   {r['tax']:.2f}")
        print(f"  Total Deduction:   {r['total_deduction']:.2f}")
        print(f"  Net Salary:        {r['net_salary']:.2f}\n")

if __name__ == "__main__":
    run_data_parallelism()