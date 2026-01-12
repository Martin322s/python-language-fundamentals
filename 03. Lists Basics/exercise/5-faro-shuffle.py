cards = input().split()
shuffles_count = int(input())

for _ in range(shuffles_count):
    middle = len(cards) // 2
    left = cards[:middle]
    right = cards[middle:]

    shuffled = []
    for i in range(middle):
        shuffled.append(left[i])
        shuffled.append(right[i])

    cards = shuffled

print(cards)