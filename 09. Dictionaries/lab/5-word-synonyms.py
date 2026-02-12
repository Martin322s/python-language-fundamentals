words_count = int(input())
synonyms_dict = {}

for _ in range(words_count):
	word = input()
	synonym = input()

	if word not in synonyms_dict:
		synonyms_dict[word] = []
	
	synonyms_dict[word].append(synonym)

for key in synonyms_dict.keys():
	print(f"{key} - {', '.join(synonyms_dict[key])}")