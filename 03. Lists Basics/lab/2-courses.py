courses_count = int(input())

courses_list = []

for i in range(0, courses_count):
	current_course = input()
	courses_list[i] = current_course

print(courses_list)