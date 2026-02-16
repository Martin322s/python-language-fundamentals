n = int(input())

for _ in range(n):
    line = input()

    start_name = line.index("@") + 1
    end_name = line.index("|")
    name = line[start_name:end_name]
    
    start_age = line.index("#") + 1
    end_age = line.index("*")
    age = line[start_age:end_age]

    print(f"{name} is {age} years old.")