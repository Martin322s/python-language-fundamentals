divisor = int(input())
bound = int(input())

start_integer = bound

while True:
	if start_integer % divisor == 0 and start_integer <= bound:
		print(start_integer)
		break
	else:
		start_integer -= 1