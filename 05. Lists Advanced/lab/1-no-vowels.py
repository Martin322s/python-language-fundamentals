text = input()

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = [el for el in text if el not in vowels]

print(*result, sep='')