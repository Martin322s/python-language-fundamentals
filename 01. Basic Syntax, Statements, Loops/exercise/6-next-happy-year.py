year = int(input())
year += 1

while True:
    y = str(year)
    
    a = y[0]
    b = y[1]
    c = y[2]
    d = y[3]

    if a != b and a != c and a != d and b != c and b != d and c != d:
        print(year)
        break

    year += 1