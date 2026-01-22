substrings = input().split(", ")
strings = input().split(", ")

result = [part for part in substrings if any(part in string for string in strings)]
print(result)