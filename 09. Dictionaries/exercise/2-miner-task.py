resources = {}

while True:
    resource = input()
    if resource == "stop":
        break
    qty = int(input())

    resources[resource] = resources.get(resource, 0) + qty

for r, q in resources.items():
    print(f"{r} -> {q}")