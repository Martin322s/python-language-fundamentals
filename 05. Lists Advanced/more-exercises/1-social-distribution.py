def solve():
    population = list(map(int, input().split(", ")))
    min_wealth = int(input())
    n = len(population)

    if sum(population) < min_wealth * n:
        print("No equal distribution possible")
        return

    for i in range(n):
        if population[i] < min_wealth:
            needed = min_wealth - population[i]

            richest_index = population.index(max(population))
            population[i] += needed
            population[richest_index] -= needed

    print(population)


solve()