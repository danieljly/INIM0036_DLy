
import networkx                                                                   
import pickle
""" RUN THIS FIRST """
# GENERATES THE DIFFERENT POPULATIONS WITH SAME NUMBERS OF CONNECTIONS, JUST ASSORTED DIFFERENTLY

# number of individuals
nodes = 10000
# average size of the contact network per individual
connections = 6

# parameters of transmission (set to covid)
beta = 0.155
sigma = 1 / 5.2
gamma = 1 / 12.39

# create a number of graphs 
for i in range(10):
    # this type of graph (powerlaw or barabasi albert) assumes the presence of superspreaders
    baseGraph = networkx.barabasi_albert_graph(n=nodes, m=connections, seed = 12)
    # we save the graph
    pickle.dump(baseGraph, open('socialgraph_' + str(i), "wb" ) )
