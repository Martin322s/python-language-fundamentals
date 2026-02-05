class Email:
	def __init__(self, sender, receiver, content, is_sent = False):
		self.sender = sender
		self.receiver = receiver
		self.content = content
		self.is_sent = is_sent

	def send(self):
		self.is_sent = True

	def get_info(self):
		return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"
	
info = input()
result = []

while info != "Stop":
	sender, receiver, content = info.split(" ")
	result.append(Email(sender, receiver, content))

	info = input()

indices = [int(x) for x in input().split(", ")]

for i in indices:
	result[i].send()
	
for object in result:
	print(object.get_info())