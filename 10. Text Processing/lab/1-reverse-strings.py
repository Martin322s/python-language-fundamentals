word = input()
words_list = []

while not word == "end":
	words_list.append(word)
	word = input()
 
reversed_words_list = [w[::-1] for w in words_list]

for i in range(len(reversed_words_list)):
    print(f"{words_list[i]} = {reversed_words_list[i]}")