import numpy as np
import pandas as pd
nodes = 10000
superspreaderProportion = 0.2
generalpopulationProportion = (1 - superspreaderProportion)
generalpopulationNumber = nodes * generalpopulationProportion
superspreaderNumber = nodes * superspreaderProportion


VaccineBudgetProportion = range(10, 110, 10)
superspreaderVaccineCompliance = range(0, 110, 10)

vaccine_budget_data = []
superspreader_compliance_data = []
relative_general_population_compliance_data = []

for p in VaccineBudgetProportion:
    for c in superspreaderVaccineCompliance:
        vaccinebudget = int((p/100)*nodes)
        superspreaderVaccineNumber = (c/100)*superspreaderNumber
        if superspreaderVaccineNumber > vaccinebudget:
            superspreaderVaccineNumber = vaccinebudget
        generalpopulationvaccineNumber = int(vaccinebudget - superspreaderVaccineNumber)
        if generalpopulationvaccineNumber < 0:
            generalpopulationvaccineNumber = 0
        if generalpopulationvaccineNumber > generalpopulationNumber:
            generalpopulationvaccineNumber = generalpopulationNumber
        relativegeneralpopulationcompliance = (generalpopulationvaccineNumber/generalpopulationNumber)*100
        vaccine_budget_data.append(p)
        superspreader_compliance_data.append(c)
        relative_general_population_compliance_data.append(relativegeneralpopulationcompliance)

data = {"Vaccine Budget (% of population)": vaccine_budget_data,
        "Superspreader Compliance (% relative to superspreader subpopulation)": superspreader_compliance_data,
        "Relative General Population Compliance (% relative to general population subpopulation)": relative_general_population_compliance_data}

df = pd.DataFrame(data, columns=["Vaccine Budget (% of population)",
                                 "Superspreader Compliance (% relative to superspreader subpopulation)",
                                 "Relative General Population Compliance (% relative to general population subpopulation)"])

df.to_csv("/Volumes/Seagate/seagate/codeSkeleton_modded_DLy_NEW/ConversionTables/" + "_generalpopulationcompliance" + ".csv", index=False, header=True)