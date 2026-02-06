neighbourhood = [int(house) for house in input().split("@")]

command = input()
position = 0

while not command == "Love!":
	jump_length = int(command.split(" ")[1])
	position += jump_length

	if position >= len(neighbourhood):
		position = 0

	if neighbourhood[position] == 0:
		print(f"Place {position} already had Valentine's day.")
	else:
		neighbourhood[position] -= 2
		
		if neighbourhood[position] == 0:
			print(f"Place {position} has Valentine's day.")

	command = input()

print(f"Cupid's last position was {position}.")

result_neighbourhood = [x for x in neighbourhood if x != 0]

if len(result_neighbourhood) == 0:
	print("Mission was successful.")
else:
	print(f"Cupid has failed {len(result_neighbourhood)} places.")