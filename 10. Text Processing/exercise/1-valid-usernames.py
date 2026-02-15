usernames = input().split(", ")

for username in usernames:
    if not (3 <= len(username) <= 16):
        continue
    
    valid = True
    for ch in username:
        if not (ch.isalnum() or ch == "-" or ch == "_"):
            valid = False
            break
    
    if valid:
        print(username)