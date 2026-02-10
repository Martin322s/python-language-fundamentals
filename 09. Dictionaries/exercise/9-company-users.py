companies = {}

while True:
    line = input()
    if line == "End":
        break

    company, emp_id = line.split(" -> ")

    if company not in companies:
        companies[company] = []

    if emp_id not in companies[company]:
        companies[company].append(emp_id)

for company, ids in companies.items():
    print(company)
    for emp_id in ids:
        print(f"-- {emp_id}")