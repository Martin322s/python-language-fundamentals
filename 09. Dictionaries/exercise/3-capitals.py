countries = input().split(", ")
capitals = input().split(", ")

cap_dict = {country: capital for country, capital in zip(countries, capitals)}

for country, capital in cap_dict.items():
    print(f"{country} -> {capital}")