import pickle
import pandas as pd
import numpy as np
from scipy import stats

vaccine_budget = []
superspreader_compliance = []
peak_percentage_infected_mean = []
peak_percentage_infected_sd = []
peak_percentage_infected_CI = []
nodes = 10000

vaccine_budget.append(0)
superspreader_compliance.append("N/A")
list = []
for i in range(10):
     model1 = pickle.load(open("_0percentvaccinebudget" + str(i), "rb"))
     peak = 100 * (max(model1.numI) / nodes)
     print("Percentage of people infected at peak is " + str(peak))
     list.append(peak)

z = stats.zscore(list)
for num in z:
    if num > 3:
        list.pop(num.index)
mean = np.mean(list)
peak_percentage_infected_mean.append(mean)
sd = np.std(list)
peak_percentage_infected_sd.append(sd)
CI = 1.96*sd
peak_percentage_infected_CI.append(CI)



list = []
for n in range(10, 90, 10):
     for x in range(0, 110, 10):
         for i in range(10):
             model1 = pickle.load(open("_" + str(n) + "percentvaccinebudget" + str(x) + "percentsuperspreadercompliance" + str(i), "rb"))
             peak = 100 * (max(model1.numI) / nodes)
             print("Percentage of people infected at peak is " + str(peak))
             list.append(peak)
         z = stats.zscore(list)
         for num in z:
             if num > 3:
                 list.pop(num.index)
         vaccine_budget.append(n)
         superspreader_compliance.append(x)
         mean = np.mean(list)
         peak_percentage_infected_mean.append(mean)
         sd = np.std(list)
         peak_percentage_infected_sd.append(sd)
         CI = 1.96 * sd
         peak_percentage_infected_CI.append(CI)
         list = []



list = []
for n in range(90, 110, 10):
    list = []
    zscorelist = []
    for x in range(0, 110, 10):
        for i in range(10):
            model1=pickle.load(open("_" + str(n) + "percentvaccinebudget" + str(x)+ "percentsuperspreadercompliance" + str(i), "rb"))
            percentage_people_vaccinated = (80+(x*0.2))
            if percentage_people_vaccinated > n:
                percentage_people_vaccinated = n
            # in order to compute the amount of superpreaders taking the vaccine
            peak = 100*(max(model1.numI)/nodes)
            print("Percentage of people infected at peak is " + str(peak))
            list.append(peak)
        zscorelist.clear()
        for num in stats.zscore(list):
            zscorelist.append(num)
        for m in zscorelist:
            if m > 3:
                list.pop(m.index)
        vaccine_budget.append(n)
        superspreader_compliance.append(x)
        mean = np.mean(list)
        peak_percentage_infected_mean.append(mean)
        sd = np.std(list)
        peak_percentage_infected_sd.append(sd)
        CI = 1.96 * sd
        peak_percentage_infected_CI.append(CI)
        list = []
        zscorelist = []


    data = {"Vaccine Budget (% of population)": vaccine_budget,
            "Superspreader Compliance (% relative to superspreader subpopulation)": superspreader_compliance,
            "Peak Infected Mean": peak_percentage_infected_mean,
            "Peak Infected Standard Deviation)": peak_percentage_infected_sd,
            "Peak Infected 95% Confidence Interval (±)": peak_percentage_infected_CI
            }
    df = pd.DataFrame(data, columns=["Vaccine Budget (% of population)",
                                     "Superspreader Compliance (% relative to superspreader subpopulation)",
                                     "Peak Infected Mean",
                                     "Peak Infected Standard Deviation)",
                                     "Peak Infected 95% Confidence Interval (±)"
                                     ])
    df.to_csv("/Volumes/Seagate/seagate/codeSkeleton_modded_DLy_NEW/Processed_Data/" + "peak_mean_sd_95percentCI_processed_data_no_outliers_z_score" + ".csv",
        index=False, header=True)