chars_count = int(input())
chars_sum = 0
for _ in range(chars_count):
	current_char = input()
	chars_sum += ord(current_char)

print(f'The sum equals: {chars_sum}')