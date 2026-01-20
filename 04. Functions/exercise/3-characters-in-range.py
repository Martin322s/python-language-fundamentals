def characters_in_range(a, b):
    start = ord(a)
    end = ord(b)
    result = []

    for code in range(start + 1, end):
        result.append(chr(code))

    return " ".join(result)


char1 = input()
char2 = input()

print(characters_in_range(char1, char2))