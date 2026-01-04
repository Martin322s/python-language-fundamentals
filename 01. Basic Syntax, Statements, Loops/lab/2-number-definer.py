number = float(input())
result = ""

if number == 0:
	result = "zero"
elif number > 0:
	result = "positive"
elif number < 0:
	result = "negative"

if abs(number) < 1 and abs(number) != 0:
	result = "small " + result
elif abs(number) > 1000000:
	result = "large " + result

print(result)