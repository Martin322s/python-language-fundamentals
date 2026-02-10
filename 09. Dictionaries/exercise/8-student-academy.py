n = int(input())
students = {}

for _ in range(n):
    name = input()
    grade = float(input())

    if name not in students:
        students[name] = []
    students[name].append(grade)

for name, grades in students.items():
    avg = sum(grades) / len(grades)
    if avg >= 4.50:
        print(f"{name} -> {avg:.2f}")