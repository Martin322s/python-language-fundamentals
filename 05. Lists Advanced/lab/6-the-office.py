happiness = list(map(int, input().split()))
factor = int(input())

improved = [x * factor for x in happiness]
average = sum(improved) / len(improved)

happy_count = sum(1 for x in improved if x >= average)
total = len(improved)

if happy_count >= total / 2:
    print(f"Score: {happy_count}/{total}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total}. Employees are not happy!")