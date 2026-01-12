factor = int(input())
count = int(input())

result_list = []
base = 0

for _ in range(count):
	base += factor
	result_list.append(base)

print(result_list)