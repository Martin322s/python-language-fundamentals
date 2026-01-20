def exchange(nums, index):
    if index < 0 or index >= len(nums):
        print("Invalid index")
        return nums
    return nums[index + 1:] + nums[:index + 1]


def get_max_index(nums, parity):
    best_value = None
    best_index = -1

    for i, value in enumerate(nums):
        if value % 2 == parity:
            if best_value is None or value >= best_value:
                best_value = value
                best_index = i

    if best_index == -1:
        print("No matches")
    else:
        print(best_index)


def get_min_index(nums, parity):
    best_value = None
    best_index = -1

    for i, value in enumerate(nums):
        if value % 2 == parity:
            if best_value is None or value <= best_value:
                best_value = value
                best_index = i

    if best_index == -1:
        print("No matches")
    else:
        print(best_index)


def first_count(nums, count, parity):
    if count > len(nums):
        print("Invalid count")
        return

    result = [x for x in nums if x % 2 == parity]
    result = result[:count]
    print(result)


def last_count(nums, count, parity):
    if count > len(nums):
        print("Invalid count")
        return

    result = [x for x in nums if x % 2 == parity]
    result = result[-count:]
    print(result)


numbers = list(map(int, input().split()))

while True:
    command_line = input()
    if command_line == "end":
        break

    parts = command_line.split()
    command = parts[0]

    if command == "exchange":
        index = int(parts[1])
        numbers = exchange(numbers, index)

    elif command == "max":
        even_odd = parts[1]
        if even_odd == "even":
            get_max_index(numbers, 0)
        else:
            get_max_index(numbers, 1)

    elif command == "min":
        even_odd = parts[1]
        if even_odd == "even":
            get_min_index(numbers, 0)
        else:
            get_min_index(numbers, 1)

    elif command == "first":
        count = int(parts[1])
        even_odd = parts[2]
        if even_odd == "even":
            first_count(numbers, count, 0)
        else:
            first_count(numbers, count, 1)

    elif command == "last":
        count = int(parts[1])
        even_odd = parts[2]
        if even_odd == "even":
            last_count(numbers, count, 0)
        else:
            last_count(numbers, count, 1)

print(numbers)