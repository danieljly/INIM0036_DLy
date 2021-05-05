import pickle
import matplotlib.pyplot as plt
import numpy as np
import ipdb

nodes= 10000
# population size
"""" DO NOT CHANGE UNLESS YOU WANT TO CHANGE THE PROPORTION OF PEOPLE TITLED SUPERSPREADERS"""
superspreaderProportion = 0.2
generalpopulationProportion = (1 - superspreaderProportion)
# Defining proportions of superspreaders vs general population

superspreaderNumber = int(superspreaderProportion * nodes)
# Number of superspreaders within the population
generalpopulationNumber = int(generalpopulationProportion * nodes)
# Number of 'general population' in the population - i.e. non-superspreaders

fig, axs = plt.subplots(figsize = (8.3, 11.7))


for i in range(0,1):
    baseGraph = pickle.load(open('socialgraph_' + str(i), "rb"))
    degree_individuals = [d for n, d in baseGraph.degree()]
    sorted_degree_sequence = sorted(degree_individuals)
    superSpreadersdegree = sorted_degree_sequence[-superspreaderNumber - 1:-1]
    generalPopulationdegree = sorted_degree_sequence[:generalpopulationNumber]
    axs.hist(superSpreadersdegree, bins = 500)
    axs.set_title("Social Graph " + str(i) + ": Connections by Number of Nodes for Superspreaders")
    axs.set_xlabel("No. of connections")
    axs.set_ylabel("No. of nodes/ people")
    # axs.hist(generalPopulationdegree)
    # axs.set_title("Social Graph " + str(i) + ": Connections by Nodes for General Population")
    # axs.set_xlabel("No. of connections")
    # axs.set_ylabel("No. of nodes/ people")

plt.tight_layout()
plt.show()