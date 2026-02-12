characters_list = input().split(", ")
ascii_codes = [ord(x) for x in characters_list]
ascii_dict = {k:v for (k,v) in zip(characters_list, ascii_codes) }

print(ascii_dict)