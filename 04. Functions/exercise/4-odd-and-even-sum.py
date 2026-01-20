def odd_even_sum(number):
    odd_sum = 0
    even_sum = 0

    for digit in number:
        d = int(digit)
        if d % 2 == 0:
            even_sum += d
        else:
            odd_sum += d

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


num = input()
print(odd_even_sum(num))