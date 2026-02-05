class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            names = ", ".join(self.mammals)
            species_print = "Mammals"
        elif species == "fish":
            names = ", ".join(self.fishes)
            species_print = "Fishes"
        elif species == "bird":
            names = ", ".join(self.birds)
            species_print = "Birds"

        return f"{species_print} in {self.name}: {names}\nTotal animals: {Zoo.__animals}"

zoo_name = input()
zoo = Zoo(zoo_name)

animals_count = int(input())

for _ in range(animals_count):
    species, name = input().split()
    zoo.add_animal(species, name)

searched_species = input()

print(zoo.get_info(searched_species))