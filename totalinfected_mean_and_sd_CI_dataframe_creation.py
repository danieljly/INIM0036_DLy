import pickle
import pandas as pd
import numpy as np
from scipy import stats


vaccine_budget = []
superspreader_compliance = []
total_percentage_infected_mean = []
total_percentage_infected_sd = []
total_percentage_infected_CI = []
nodes = 10000

vaccine_budget.append(0)
superspreader_compliance.append("N/A")
list = []
for i in range(10):
     model1 = pickle.load(open("_0percentvaccinebudget" + str(i), "rb"))
     inf = 100 * ((nodes - model1.numS[-1]) / nodes)
     print("Total percentage of infected is " + str(inf))
     list.append(inf)

z = stats.zscore(list)
for num in z:
    if num > 3:
        list.pop(num.index)
mean = np.mean(list)
total_percentage_infected_mean.append(mean)
sd = np.std(list)
total_percentage_infected_sd.append(sd)
CI = 1.96* sd
total_percentage_infected_CI.append(CI)



list =[]
for n in range(10, 90, 10):
     for x in range(0, 110, 10):
         for i in range(10):
             model1 = pickle.load(open("_" + str(n) + "percentvaccinebudget" + str(x) + "percentsuperspreadercompliance" + str(i), "rb"))
             inf = (100 * ((nodes - model1.numS[-1]) / nodes)) - n
             print("Total percentage of infected is " + str(inf))
             list.append(inf)
         z = stats.zscore(list)
         for num in z:
             if num > 3:
                 list.pop(num.index)
         vaccine_budget.append(n)
         superspreader_compliance.append(x)
         mean = np.mean(list)
         total_percentage_infected_mean.append(mean)
         sd = np.std(list)
         total_percentage_infected_sd.append(sd)
         CI = 1.96 * sd
         total_percentage_infected_CI.append(CI)
         list = []



list = []
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
            print("Total percentage of infected is " + str(inf))
            list.append(inf)
        z = stats.zscore(list)
        for num in z:
            if num > 3:
                list.pop(num.index)
        vaccine_budget.append(n)
        superspreader_compliance.append(x)
        mean = np.mean(list)
        total_percentage_infected_mean.append(mean)
        sd = np.std(list)
        total_percentage_infected_sd.append(sd)
        CI = 1.96 * sd
        total_percentage_infected_CI.append(CI)
        list = []

    data = {"Vaccine Budget (% of population)": vaccine_budget,
            "Superspreader Compliance (% relative to superspreader subpopulation)": superspreader_compliance,
            "Total Infected Mean": total_percentage_infected_mean,
            "Total Infected Standard Deviation)": total_percentage_infected_sd,
            "Total Infected 95% Confidence Interval (±)": total_percentage_infected_CI
            }
    df = pd.DataFrame(data, columns=["Vaccine Budget (% of population)",
                                     "Superspreader Compliance (% relative to superspreader subpopulation)",
                                     "Total Infected Mean",
                                     "Total Infected Standard Deviation)",
                                     "Total Infected 95% Confidence Interval (±)"
                                     ])
    df.to_csv("/Volumes/Seagate/seagate/codeSkeleton_modded_DLy_NEW/Processed_Data/" + "total_mean_sd_95percentCI_processed_data_no_outliers_z_score" + ".csv",
        index=False, header=True)

