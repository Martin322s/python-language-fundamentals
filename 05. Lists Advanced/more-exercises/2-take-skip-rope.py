def solve():
    text = input()

    numbers = []
    chars = []

    for ch in text:
        if ch.isdigit():
            numbers.append(int(ch))
        else:
            chars.append(ch)

    take_list = []
    skip_list = []

    for i in range(len(numbers)):
        if i % 2 == 0:
            take_list.append(numbers[i])
        else:
            skip_list.append(numbers[i])

    result = []
    index = 0

    for take, skip in zip(take_list, skip_list):
        result.extend(chars[index:index + take])
        index += take

        index += skip

        if index >= len(chars):
            break

    print("".join(result))


solve()