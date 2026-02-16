import re

regex = r"(?P<Day>\d{2})(?P<Separator>[-/\.])(?P<Month>[A-Z][a-z]{2})(?P=Separator)(?P<Year>\d{4})"

txt = input()

valid_dates = re.finditer(regex, txt)

for date in valid_dates:
    current_date = date.groupdict()
    print(f"Day: {current_date['Day']}, Month: {current_date['Month']}, Year: {current_date['Year']}")