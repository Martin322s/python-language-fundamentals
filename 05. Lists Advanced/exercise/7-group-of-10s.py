numbers = list(map(int, input().split(", ")))

max_num = max(numbers)
current_group = 10

while current_group <= max_num:
    group_list = [num for num in numbers if num <= current_group]
    print(f"Group of {current_group}'s: {group_list}")
    numbers = [num for num in numbers if num not in group_list]
    current_group += 10