words = input().lower().split()

occurrences = {}

for word in words:
    occurrences[word] = occurrences.get(word, 0) + 1

result = [word for word in occurrences if occurrences[word] % 2 == 1]

print(" ".join(result))