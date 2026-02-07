import threading, time

def compute_gwa(grades):
    gwa = sum(grades) / len(grades)
    print(f"[Thread] Calculated GWA: {gwa}")

def main():
    grades_list = []
    n = int(input("Enter number of subjects: "))

    for i in range(n):
        grade = float(input(f"Enter grade for subject {i + 1}: "))
        grades_list.append(grade)

    t = threading.Thread(target=compute_gwa, args=(grades_list,))
    start_time = time.time_ns()
    t.start()
    t.join()
    end_time = time.time_ns()

    execution_time = end_time - start_time
    ns_to_s = execution_time / 1000000000

    print(f"Execution time is {execution_time} nanoseconds, and {ns_to_s} in seconds")

if __name__ == "__main__":
    main()
