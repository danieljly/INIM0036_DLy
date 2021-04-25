import pickle
import matplotlib.pyplot as plt

fig, axs = plt.subplots(nrows = 2, ncols= 5, figsize = (8.3, 11.7))
x = 0
y = 0

for i in range(10):
    baseGraph = pickle.load(open('socialgraph_' + str(i), "rb"))
    degree_individuals = [d for n, d in baseGraph.degree()]
    axs[x, y].hist(degree_individuals, bins = 500)
    axs[x, y].set_title("Social Graph " + str(i) + ": Connections by Number of Nodes/ People", fontsize = "xx-small")
    axs[x, y].set_xlabel("No. of connections", fontsize = "xx-small")
    axs[x, y].set_ylabel("No. of nodes/ people", fontsize = "xx-small")
    y += 1
    if y == 5:
        x = 1
        y = 0

plt.tight_layout()
plt.show()
