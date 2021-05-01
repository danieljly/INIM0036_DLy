import pickle
import matplotlib.pyplot as plt

# datastore = {"0% Vaccine Budget": []}
datastore = {}

# for a in range(30,40,10):
#     for b in range(100,110,10):
#         datastore[str(a) + "% Vaccine Budget " + str(b) + "% Superspreader Compliance"] = []
#
# for a in range(40,60,10):
#     for b in range(90,110,10):
#         datastore[str(a) + "% Vaccine Budget " + str(b) + "% Superspreader Compliance"] = []
# #
# for a in range(60,80,10):
#     for b in range(80,110,10):
#         datastore[str(a) + "% Vaccine Budget " + str(b) + "% Superspreader Compliance"] = []
#
# for a in range(80,90,10):
#     for b in range(70,110,10):
#         datastore[str(a) + "% Vaccine Budget " + str(b) + "% Superspreader Compliance"] = []
#
# datastore["90% Vaccine Budget 50% Superspreader Compliance"]=[]
#
# for a in range(90,100,10):
#     for b in range(70,110,10):
#         datastore[str(a) + "% Vaccine Budget " + str(b) + "% Superspreader Compliance"] = []
# #
for a in range(100,110,10):
    for b in range(70,110,10):
        datastore[str(a) + "% Vaccine Budget " + str(b) + "% Superspreader Compliance"] = []


nodes = 10000

# list = []
# for i in range(10):
#      model1 = pickle.load(open("_0percentvaccinebudget" + str(i), "rb"))
#      inf = 100 * ((nodes - model1.numS[-1]) / nodes)
#      print("Total percentage of infected is " + str(inf))
#      list.append(inf)
# datastore["0% Vaccine Budget"] = list


# list =[]
# for n in range(30, 40, 10):
#      for x in range(100, 110, 10):
#          for i in range(10):
#              model1 = pickle.load(open("_" + str(n) + "percentvaccinebudget" + str(x) + "percentsuperspreadercompliance" + str(i), "rb"))
#              inf = (100 * ((nodes - model1.numS[-1]) / nodes)) - n
#              print("Total percentage of infected is " + str(inf))
#              list.append(inf)
#          datastore[str(n) + "% Vaccine Budget " + str(x) + "% Superspreader Compliance"] = list
#          list = []
#
# list =[]
# for n in range(40, 60, 10):
#      for x in range(90, 110, 10):
#          for i in range(10):
#              model1 = pickle.load(open("_" + str(n) + "percentvaccinebudget" + str(x) + "percentsuperspreadercompliance" + str(i), "rb"))
#              inf = (100 * ((nodes - model1.numS[-1]) / nodes)) - n
#              print("Total percentage of infected is " + str(inf))
#              list.append(inf)
#          datastore[str(n) + "% Vaccine Budget " + str(x) + "% Superspreader Compliance"] = list
#          list = []
#
# list =[]
# for n in range(60, 80, 10):
#      for x in range(80, 110, 10):
#          for i in range(10):
#              model1 = pickle.load(open("_" + str(n) + "percentvaccinebudget" + str(x) + "percentsuperspreadercompliance" + str(i), "rb"))
#              inf = (100 * ((nodes - model1.numS[-1]) / nodes)) - n
#              print("Total percentage of infected is " + str(inf))
#              list.append(inf)
#          datastore[str(n) + "% Vaccine Budget " + str(x) + "% Superspreader Compliance"] = list
#          list = []
#
# list = []
# for n in range(80, 90, 10):
#     for x in range(70, 110, 10):
#         for i in range(10):
#             model1=pickle.load(open("_" + str(n) + "percentvaccinebudget" + str(x)+ "percentsuperspreadercompliance" + str(i), "rb"))
#             percentage_people_vaccinated = (80+(x*0.2))
#             if percentage_people_vaccinated > n:
#                 percentage_people_vaccinated = n
#             # in order to compute the amount of superpreaders taking the vaccine
#             inf = (100*((nodes - model1.numS[-1])/nodes)) - percentage_people_vaccinated
#             if inf <0:
#                 inf = 0
#             print("Total percentage of infected is " + str(inf))
#             list.append(inf)
#         datastore[str(n) + "% Vaccine Budget " + str(x) + "% Superspreader Compliance"] = list
#         list = []

# list = []
# for n in range(90, 100, 10):
#     for x in range(50, 60, 10):
#         for i in range(10):
#             model1=pickle.load(open("_" + str(n) + "percentvaccinebudget" + str(x)+ "percentsuperspreadercompliance" + str(i), "rb"))
#             percentage_people_vaccinated = (80+(x*0.2))
#             if percentage_people_vaccinated > n:
#                 percentage_people_vaccinated = n
#             # in order to compute the amount of superpreaders taking the vaccine
#             inf = (100*((nodes - model1.numS[-1])/nodes)) - percentage_people_vaccinated
#             if inf <0:
#                 inf = 0
#             print("Total percentage of infected is " + str(inf))
#             list.append(inf)
#         datastore[str(n) + "% Vaccine Budget " + str(x) + "% Superspreader Compliance"] = list
#         list = []
# #
#
# list = []
# for n in range(90, 100, 10):
#     for x in range(70, 110, 10):
#         for i in range(10):
#             model1=pickle.load(open("_" + str(n) + "percentvaccinebudget" + str(x)+ "percentsuperspreadercompliance" + str(i), "rb"))
#             percentage_people_vaccinated = (80+(x*0.2))
#             if percentage_people_vaccinated > n:
#                 percentage_people_vaccinated = n
#             # in order to compute the amount of superpreaders taking the vaccine
#             inf = (100*((nodes - model1.numS[-1])/nodes)) - percentage_people_vaccinated
#             if inf <0:
#                 inf = 0
#             print("Total percentage of infected is " + str(inf))
#             list.append(inf)
#         datastore[str(n) + "% Vaccine Budget " + str(x) + "% Superspreader Compliance"] = list
#         list = []
# # #
#
list = []
for n in range(100, 110, 10):
    for x in range(70, 110, 10):
        for i in range(10):
            model1=pickle.load(open("_" + str(n) + "percentvaccinebudget" + str(x)+ "percentsuperspreadercompliance" + str(i), "rb"))
            percentage_people_vaccinated = (80+(x*0.2))
            if percentage_people_vaccinated > n:
                percentage_people_vaccinated = n
            # in order to compute the amount of superpreaders taking the vaccine
            inf = (100*((nodes - model1.numS[-1])/nodes)) - percentage_people_vaccinated
            if inf <0:
                inf = 0
            print("Total percentage of infected is " + str(inf))
            list.append(inf)
        datastore[str(n) + "% Vaccine Budget " + str(x) + "% Superspreader Compliance"] = list
        list = []


fig, ax = plt.subplots()
ax.boxplot(datastore.values(), vert = False)
ax.set_yticklabels(datastore.keys(), fontsize = 7)
plt.xlabel('total % of people infected')
plt.tight_layout()
plt.show()
# generates a boxplot with the data
