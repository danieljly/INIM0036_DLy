from seirsplus2.models import *
from seirsplus2.networks import *
from seirsplus2.sim_loops import *
from seirsplus2.utilities import *
import networkx
import matplotlib.pyplot as pyplot
import pickle
import matplotlib.pyplot as plt
import pandas as pd

total_percentage_infected = []
percentage_people_infected_at_peak = []
nodes = 10000

for n in range(10, 90, 10):
     for x in range(0, 110, 10):
         for i in range(10):
             model1 = pickle.load(open("_" + str(n) + "percentvaccinebudget" + str(x) + "percentsuperspreadercompliance" + str(i), "rb"))
             inf = (100 * ((nodes - model1.numS[-1]) / nodes)) - n
             peak = 100 * (max(model1.numI) / nodes)
             print("Total percentage of infected is " + str(inf))
             print("Percentage of people infected at peak is " + str(peak))
             total_percentage_infected.append(inf)
             percentage_people_infected_at_peak.append(peak)
         data = {"Total % of people infected": total_percentage_infected, "% of people infected at peak": percentage_people_infected_at_peak}
         df = pd.DataFrame(data, columns=["Total % of people infected", "% of people infected at peak"])
         df.to_csv("/Volumes/Seagate/seagate/codeSkeleton_modded_DLy_NEW/DataFramesFIX/" + "_" + str(n) + "percentvaccinebudget" + str(x) + "percentsuperspreadercompliance" + ".csv", index=False, header=True)
         total_percentage_infected = []
         percentage_people_infected_at_peak = []



for n in range(90, 110, 10):
    for x in range(0, 110, 10):
        for i in range(10):
            model1=pickle.load(open("_" + str(n) + "percentvaccinebudget" + str(x)+ "percentsuperspreadercompliance" + str(i), "rb"))
            percentage_people_vaccinated = (80+(x*0.2))
            if percentage_people_vaccinated > n:
                percentage_people_vaccinated = n
            # in order to compute the amount of superpreaders taking the vaccine
            inf = (100*((nodes - model1.numS[-1])/nodes)) - percentage_people_vaccinated
            if inf <0:
                inf = 0
            peak = 100*(max(model1.numI)/nodes)
            print("Total percentage of infected is " + str(inf))
            print("Percentage of people infected at peak is " + str(peak))
            total_percentage_infected.append(inf)
            percentage_people_infected_at_peak.append(peak)
        data = {"Total % of people infected": total_percentage_infected, "% of people infected at peak": percentage_people_infected_at_peak}
        df = pd.DataFrame(data, columns=["Total % of people infected", "% of people infected at peak"])
        df.to_csv("/Volumes/Seagate/seagate/codeSkeleton_modded_DLy_NEW/DataFramesFIX/" + "_" + str(n) + "percentvaccinebudget" + str(x) + "percentsuperspreadercompliance" +".csv", index = False, header=True)
        total_percentage_infected = []
        percentage_people_infected_at_peak = []

for i in range(10):
     model1 = pickle.load(open("_0percentvaccinebudget" + str(i), "rb"))
     inf = 100 * ((nodes - model1.numS[-1]) / nodes)
     peak = 100 * (max(model1.numI) / nodes)
     print("Total percentage of infected is " + str(inf))
     print("Percentage of people infected at peak is " + str(peak))
     total_percentage_infected.append(inf)
     percentage_people_infected_at_peak.append(peak)
data = {"Total % of people infected": total_percentage_infected, "% of people infected at peak": percentage_people_infected_at_peak}
df = pd.DataFrame(data, columns=["Total % of people infected", "% of people infected at peak"])
# TODO: CHANGE THE FILE PATH TO YOUR DESKTOP APPROPRIATE PATH
df.to_csv("/Volumes/Seagate/seagate/codeSkeleton_modded_DLy_NEW/DataFramesFIX/" + "_0percentvaccinebudget" + ".csv", index=False, header=True)