def loading_bar(num):
    percent_count = num // 10
    filled = "%" * percent_count
    empty = "." * (10 - percent_count)

    if num == 100:
        return f"100% Complete!\n[{filled}]"
    else:
        return f"{num}% [{filled}{empty}]\nStill loading..."


n = int(input())
print(loading_bar(n))