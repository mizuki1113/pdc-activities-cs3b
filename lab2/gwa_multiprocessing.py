from multiprocessing import Process
import time

def compute_gwa_mp(grades):
    gwa = sum(grades) / len(grades)
    print(f"[Process] Calculated GWA: {gwa}")

# Get grades from user
print("Enter your grades (type 'done' when finished):")
grades_list = []
while True:
    grade_input = input("Grade: ")
    if grade_input.lower() == 'done':
        break
    try:
        grade = float(grade_input)
        grades_list.append(grade)
    except:
        print("Invalid input, try again")

processes = []
for grade in grades_list:
    p = Process(target=compute_gwa_mp, args=([grade],))
    processes.append(p)
    start_time = time.time_ns()
    p.start()

for p in processes:
    p.join()
    end_time = time.time_ns()

execution_time = end_time - start_time
ns_to_s = execution_time / 1000000000

if grades_list:
    overall_gwa = sum(grades_list) / len(grades_list)
    print(f"\n[Main Process] Overall GWA: {overall_gwa:.2f}")
    print(f"Execution Time is {execution_time} nanoseconds, and {ns_to_s} in seconds")