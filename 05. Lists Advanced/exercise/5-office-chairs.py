rooms = int(input())

total_free_chairs = 0
game_on = True

for room in range(1, rooms + 1):
    chairs_str, visitors_str = input().split()
    chairs = len(chairs_str)
    visitors = int(visitors_str)

    if chairs < visitors:
        print(f"{visitors - chairs} more chairs needed in room {room}")
        game_on = False
    else:
        total_free_chairs += chairs - visitors

if game_on:
    print(f"Game On, {total_free_chairs} free chairs left")