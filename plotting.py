from seirsplus2.models import *
from seirsplus2.networks import *
from seirsplus2.sim_loops import *
from seirsplus2.utilities import *
import networkx
import matplotlib.pyplot as pyplot
import pickle
import matplotlib.pyplot as plt
import pandas as pd

fig = plt.figure()                                                                                 
ax = plt.axes()  
total_percentage_infected = []
percentage_people_infected_at_peak = []

nodes = 10000
for i in range(10):
    # load the model that we saved before (TODO: change the name of the file)
    model1 = pickle.load( open('_100percentvaccinebudget100percentsuperspreadercompliance' + str(i), "rb" ) )
    inf = 100*((nodes - model1.numS[-1])/nodes)
    peak = 100*(max(model1.numI)/nodes)
    print("Total percentage of infected is " + str(inf))
    print("Percentage of people infected at peak is " + str(peak))
    total_percentage_infected.append(inf)
    percentage_people_infected_at_peak.append(peak)
    #TODO: CHANGE LABEL OF LINES
    ax.plot(100*model1.numI/nodes, label="100% vaccine budget and 100% superspreader vaccine compliance, simulation no. " + str(i+1))

plt.xlabel('Time (t)')
# Set the y axis label of the current axis.
plt.ylabel('Percentage infected at given time')
# Set a title of the current axes.
#TODO: CHANGE THE NAME OF THE GRAPH
plt.title('Percentage of people infected with 100% vaccine budget and 100% superspreader vaccine compliance')
plt.legend()
plt.show()     