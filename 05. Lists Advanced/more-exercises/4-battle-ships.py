def solve():
    n = int(input())
    field = []

    for _ in range(n):
        field.append([int(x) for x in input().split()])

    attacks = input().split()
    destroyed = 0

    for attack in attacks:
        r_str, c_str = attack.split("-")
        r = int(r_str)
        c = int(c_str)

        if field[r][c] > 0:
            field[r][c] -= 1
            if field[r][c] == 0:
                destroyed += 1

    print(destroyed)


solve()