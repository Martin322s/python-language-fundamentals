activation_key = input()

data = input()

while not data == "Generate":
    data = data.split(">>>")
    
    if data[0] == "Slice":
        start_index = int(data[1])
        end_index = int(data[2])
        
        first_part = activation_key[:start_index]
        third_part = activation_key[end_index:]
        
        activation_key = first_part + third_part
        print(activation_key)
        
    elif data[0] == "Flip":
        state = data[1]
        start_index = int(data[2])
        end_index = int(data[3])
        
        first_part = activation_key[:start_index]
        second_part = activation_key[start_index:end_index]
        third_part = activation_key[end_index:]
        
        if state == "Upper":
            second_part = second_part.upper()
        else:
            second_part = second_part.lower()
            
        activation_key = first_part + second_part + third_part
        print(activation_key)
    
    elif data[0] == "Contains":
        substring = data[1]
        
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    
    data = input()

print(f"Your activation key is: {activation_key}")