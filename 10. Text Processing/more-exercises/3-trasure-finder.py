key = list(map(int, input().split()))

while True:
    line = input()
    if line == "find":
        break

    decrypted_chars = []
    key_index = 0

    for ch in line:
        decrypted_chars.append(chr(ord(ch) - key[key_index]))
        key_index += 1
        if key_index == len(key):
            key_index = 0

    decrypted = "".join(decrypted_chars)

    start_type = decrypted.index("&") + 1
    end_type = decrypted.index("&", start_type)
    treasure_type = decrypted[start_type:end_type]

    start_coord = decrypted.index("<") + 1
    end_coord = decrypted.index(">")
    coordinates = decrypted[start_coord:end_coord]

    print(f"Found {treasure_type} at {coordinates}")