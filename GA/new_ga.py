from functools import partial
import knapsack
import ga as genetic
from contextlib import contextmanager
import time


@contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print(f"Elapsed Time: {(end - start)}s")

things = knapsack.generate_things(22)
things = knapsack.second_example

weight_limit = 3000

print("")
print("GENETIC ALGORITHM")
print("----------")


with timer():
	population, generations = genetic.run_evolution(
		populate_func=partial(genetic.generate_population, size=10, genome_length=len(things)),
		fitness_func=partial(knapsack.fitness, things=things, weight_limit=weight_limit),
		fitness_limit=5,
		generation_limit=100
	)

sack = knapsack.from_genome(population[0], things)
knapsack.print_stats(sack)