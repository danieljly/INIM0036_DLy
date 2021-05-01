import pickle
import matplotlib.pyplot as plt

datastore = {"0% Vaccine Budget": []}

for a in range(40,60,10):
    for b in range(80,110,10):
        datastore[str(a) + "% Vaccine Budget " + str(b) + "% Superspreader Compliance"] = []

for a in range(60,80,10):
    for b in range(60,110,10):
        datastore[str(a) + "% Vaccine Budget " + str(b) + "% Superspreader Compliance"] = []

for a in range(80,100,10):
    for b in range(50,110,10):
        datastore[str(a) + "% Vaccine Budget " + str(b) + "% Superspreader Compliance"] = []

for a in range(100,110,10):
    for b in range(40,110,10):
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
for n in range(40, 60, 10):
     for x in range(80, 110, 10):
         for i in range(10):
             model1 = pickle.load(open("_" + str(n) + "percentvaccinebudget" + str(x) + "percentsuperspreadercompliance" + str(i), "rb"))
             peak = 100 * (max(model1.numI) / nodes)
             print("Percentage of people infected at peak is " + str(peak))
             list.append(peak)
         datastore[str(n) + "% Vaccine Budget " + str(x) + "% Superspreader Compliance"] = list
         list = []
# reads the pickled data for 40-50% vaccine budget, 80-100% superspreader compliances

list =[]
for n in range(60, 80, 10):
     for x in range(60, 110, 10):
         for i in range(10):
             model1 = pickle.load(open("_" + str(n) + "percentvaccinebudget" + str(x) + "percentsuperspreadercompliance" + str(i), "rb"))
             peak = 100 * (max(model1.numI) / nodes)
             print("Percentage of people infected at peak is " + str(peak))
             list.append(peak)
         datastore[str(n) + "% Vaccine Budget " + str(x) + "% Superspreader Compliance"] = list
         list = []
# reads the pickled data for 60-70% vaccine budget, 50-100% superspreader compliances


list = []
for n in range(80, 100, 10):
    for x in range(50, 110, 10):
        for i in range(10):
            model1=pickle.load(open("_" + str(n) + "percentvaccinebudget" + str(x)+ "percentsuperspreadercompliance" + str(i), "rb"))
            peak = 100 * (max(model1.numI) / nodes)
            print("Percentage of people infected at peak is " + str(peak))
            list.append(peak)
        datastore[str(n) + "% Vaccine Budget " + str(x) + "% Superspreader Compliance"] = list
        list = []
# reads the pickled data for 80-90% vaccine budget, 60-100% superspreader compliances

list =[]
for n in range(100, 110, 10):
     for x in range(40, 110, 10):
         for i in range(10):
             model1 = pickle.load(open("_" + str(n) + "percentvaccinebudget" + str(x) + "percentsuperspreadercompliance" + str(i), "rb"))
             peak = 100 * (max(model1.numI) / nodes)
             print("Percentage of people infected at peak is " + str(peak))
             list.append(peak)
         datastore[str(n) + "% Vaccine Budget " + str(x) + "% Superspreader Compliance"] = list
         list = []
# reads the pickled data for 40-50% vaccine budget, 80-100% superspreader compliances

fig, ax = plt.subplots(figsize = (8.3, 11.7))
ax.boxplot(datastore.values(), vert = False)
ax.set_yticklabels(datastore.keys(), fontsize = 10)
plt.xlabel('% of people infected at peak')
plt.tight_layout()
plt.show()
# generates a boxplot with the data