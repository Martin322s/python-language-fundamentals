def factorial(num):
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result


a = int(input())
b = int(input())

fact_a = factorial(a)
fact_b = factorial(b)

division = fact_a / fact_b
print(f"{division:.2f}")