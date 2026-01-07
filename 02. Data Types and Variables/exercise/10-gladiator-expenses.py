lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
shield_breaks = 0

for fight in range(1, lost_fights + 1):

    helmet_broken = False
    sword_broken = False

    if fight % 2 == 0:
        expenses += helmet_price
        helmet_broken = True

    if fight % 3 == 0:
        expenses += sword_price
        sword_broken = True

    if helmet_broken and sword_broken:
        expenses += shield_price
        shield_breaks += 1

        if shield_breaks % 2 == 0:
            expenses += armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")