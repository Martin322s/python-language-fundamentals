tickets = [t.strip() for t in input().split(",")]

winning_symbols = ['@', '#', '$', '^']

for ticket in tickets:
    ticket = ticket.strip()

    if len(ticket) != 20:
        print("invalid ticket")
        continue

    left = ticket[:10]
    right = ticket[10:]

    best_symbol = None
    best_length = 0

    for sym in winning_symbols:

        current = 0
        left_max = 0
        for ch in left:
            if ch == sym:
                current += 1
                left_max = max(left_max, current)
            else:
                current = 0

        current = 0
        right_max = 0
        for ch in right:
            if ch == sym:
                current += 1
                right_max = max(right_max, current)
            else:
                current = 0

        if left_max >= 6 and right_max >= 6:
            match_len = min(left_max, right_max)
            if match_len > best_length:
                best_length = match_len
                best_symbol = sym

    if best_symbol is None:
        print(f'ticket "{ticket}" - no match')
    else:
        if best_length == 10:
            print(f'ticket "{ticket}" - {best_length}{best_symbol} Jackpot!')
        else:
            print(f'ticket "{ticket}" - {best_length}{best_symbol}')