def get_grade_info(grade):
	if 2.00 <= grade and grade <= 2.99:
		return "Fail"
	elif 3.00 <= grade and grade <= 3.49:
		return "Poor"
	elif 3.50 <= grade and grade <= 4.49:
		return "Good"
	elif 4.50 <= grade and grade <= 5.49:
		return "Very Good"
	elif 5.50 <= grade and grade <= 6.00:
		return "Excellent"
	
input_grade = float(input())
grade = get_grade_info(input_grade)
print(grade)