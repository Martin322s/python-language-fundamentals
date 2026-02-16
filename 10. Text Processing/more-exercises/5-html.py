title = input()
content = input()

print(f"<h1>")
print(title)
print(f"</h1>")

print(f"<article>")
print(content)
print(f"</article>")

while True:
    comment = input()
    if comment == "end of comments":
        break

    print(f"<div>")
    print(comment)
    print(f"</div>")