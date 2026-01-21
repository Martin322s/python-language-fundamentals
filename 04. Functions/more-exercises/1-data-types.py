def data_processor(data_type, value):
    if data_type == "int":
        return int(value) * 2

    elif data_type == "real":
        result = float(value) * 1.5
        return f"{result:.2f}"

    elif data_type == "string":
        return f"${value}$"


data_type = input()
value = input()

print(data_processor(data_type, value))