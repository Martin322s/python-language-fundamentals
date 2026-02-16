import re

regex = r"(\+359 2 \d{3} \d{4})|(\+359-2-\d{3}-\d{4})\b"

phone_numbers = input()

result = re.finditer(regex, phone_numbers)

result_list = [x.group() for x in result]

print(", ".join(result_list))