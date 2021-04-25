import pickle
import matplotlib.pyplot as plt

datastore = {"0% Vaccine Budget": []}

for a in range(10,110,10):
    for b in range(0,110,10):
        datastore[str(a) + "% Vaccine Budget " + str(b) + "% Superspreader Compliance"] = []
# generates the names for all of the conditions as keys

nodes = 10000

list = []
for i in range(10):
     model1 = pickle.load(open("_0percentvaccinebudget" + str(i), "rb"))
     peak = 100 * (max(model1.numI) / nodes)
     print("Percentage of people infected at peak is " + str(peak))
     list.append(peak)
datastore["0% Vaccine Budget"] = list
# reads the pickled data for 0% vaccine budget

list =[]
for n in range(10, 90, 10):
     for x in range(0, 110, 10):
         for i in range(10):
             model1 = pickle.load(open("_" + str(n) + "percentvaccinebudget" + str(x) + "percentsuperspreadercompliance" + str(i), "rb"))
             peak = 100 * (max(model1.numI) / nodes)
             print("Percentage of people infected at peak is " + str(peak))
             list.append(peak)
         datastore[str(n) + "% Vaccine Budget " + str(x) + "% Superspreader Compliance"] = list
         list = []
# reads the pickled data for 10-80% vaccine budget, all superspreader compliances


list = []
for n in range(90, 110, 10):
    for x in range(0, 110, 10):
        for i in range(10):
            model1=pickle.load(open("_" + str(n) + "percentvaccinebudget" + str(x)+ "percentsuperspreadercompliance" + str(i), "rb"))
            peak = 100 * (max(model1.numI) / nodes)
            print("Percentage of people infected at peak is " + str(peak))
            list.append(peak)
        datastore[str(n) + "% Vaccine Budget " + str(x) + "% Superspreader Compliance"] = list
        list = []
# reads the pickled data for 90-100% vaccine budget, all superspreader compliances

fig, ax = plt.subplots(figsize = (8.3, 11.7))
ax.boxplot(datastore.values(), vert = False)
ax.set_yticklabels(datastore.keys(), fontsize = 4)
plt.show()
# generates a boxplot with the data