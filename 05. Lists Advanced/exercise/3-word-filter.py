text = input().split()

even_words = [word for word in text if len(word) % 2 == 0]

for w in even_words:
    print(w)