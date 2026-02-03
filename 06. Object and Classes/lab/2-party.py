class Party:
	def __init__(self):
		self.people = []

party = Party()

human = input()

while human != "End":
	party.people.append(human)

	human = input()

print("Going: " + ", ".join(party.people))
print("Total: " + str(len(party.people)))
