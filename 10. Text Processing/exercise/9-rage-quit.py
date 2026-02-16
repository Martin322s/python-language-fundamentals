text = input()

result_parts = []
unique_symbols = set()

i = 0
n = len(text)

while i < n:
    start = i
    while i < n and not text[i].isdigit():
        i += 1
    segment = text[start:i].upper()

    start = i
    while i < n and text[i].isdigit():
        i += 1
    repeat = int(text[start:i])

    if repeat > 0:
        result_parts.append(segment * repeat)
        unique_symbols.update(segment)

final_message = "".join(result_parts)

print(f"Unique symbols used: {len(unique_symbols)}")
print(final_message)