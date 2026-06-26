from attendance import Subject
import matplotlib.pyplot as plt

subjects = []

print("===== SMART ATTENDANCE ANALYZER =====")

try:
    n = int(input("Enter number of subjects: "))
except ValueError:
    print("Invalid input! Enter numbers only.")
    exit()

for i in range(n):
    print("\nEnter details for Subject", i + 1)

    name = input("Subject name: ")

    try:
        attended = int(input("Classes attended: "))
        total = int(input("Total classes: "))
    except ValueError:
        print("Invalid input! Enter numbers only.")
        exit()

    subjects.append(Subject(name, attended, total))

print("\n===== ATTENDANCE REPORT =====")

for sub in subjects:
    sub.report()

# GRAPH PART
names = [s.name for s in subjects]
percentages = [(s.attended / s.total) * 100 for s in subjects]

plt.bar(names, percentages)
plt.xlabel("Subjects")
plt.ylabel("Attendance %")
plt.title("Attendance Analysis")
plt.show()