def is_palindrome(num):
    return num == num[::-1]


numbers = input().split(", ")

for n in numbers:
    print(is_palindrome(n))