char1 = input()
char2 = input()
text = input()

start = ord(char1)
end = ord(char2)

low = min(start, end)
high = max(start, end)

total_sum = 0

for ch in text:
    if low < ord(ch) < high:
        total_sum += ord(ch)

print(total_sum)