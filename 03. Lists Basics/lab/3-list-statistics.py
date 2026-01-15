numbers_count = int(input())

positives_list = []
negatives_list = []
negatives_sum = 0

while numbers_count > 0:
	current_number = int(input())

	if current_number >= 0:
		positives_list.append(current_number)
	else:
		negatives_list.append(current_number)
		negatives_sum += current_number
	
	numbers_count -= 1

print(positives_list)
print(negatives_list)
print(f"Count of positives: {len(positives_list)}")
print(f"Sum of negatives: {negatives_sum}")