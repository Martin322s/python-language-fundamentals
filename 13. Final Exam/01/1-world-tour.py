stops = input()
command = input()

while True:
    if command == "Travel":
        break
    
    command_data = command.split(":")
    
    if command_data[0] == "Add Stop":
        index = int(command_data[1])
        string = command_data[2]
        
        if 0 <= index < len(stops):
            first_part = stops[:index]
            second_part = stops[index:]
            
            stops = first_part + string + second_part
        print(stops)
             
    elif command_data[0] == "Remove Stop":
        start_index = int(command_data[1])
        end_index = int(command_data[2])
        
        if 0 <= start_index < len(stops) and 0 <= end_index < len(stops):
            first_part = stops[:start_index]
            to_remove = stops[start_index:end_index + 1]
            second_part = stops[end_index + 1:]
            
            stops = first_part + second_part
        print(stops)
            
    elif command_data[0] == "Switch":
        old_string = command_data[1]
        new_string = command_data[2]
        
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
        
        print(stops)
    
    command = input()
    
print(f"Ready for world tour! Planned stops: {stops}")