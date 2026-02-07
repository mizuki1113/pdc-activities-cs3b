import threading

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
    t.start()
    t.join()

if __name__ == "__main__":
    main()
