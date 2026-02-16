text_input = input()
words_list = text_input.split(" ")

words_list = [txt * len(txt) for txt in words_list]

print("".join(words_list))