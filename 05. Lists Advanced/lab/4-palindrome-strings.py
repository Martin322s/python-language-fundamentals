words = input().split()
target = input()

palindromes = [w for w in words if w == w[::-1]]
count_target = palindromes.count(target)

print(palindromes)
print(f"Found palindrome {count_target} times")