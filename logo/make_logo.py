import msprime

x = msprime.simulate(4,mutation_rate=1,random_seed=42)

t = next(x.trees())
t.draw("logo.svg")
