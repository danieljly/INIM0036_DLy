from seirsplus2.models import *
from seirsplus2.networks import *
from seirsplus2.sim_loops import *
from seirsplus2.utilities import *
import networkx
import matplotlib.pyplot as pyplot
import pickle
import matplotlib.pyplot as plt                                                                    
import random
import numpy as np
import ipdb


""" GENERAL POPULATION DEFINITIONS """

random.seed(a = 12, version= 2)
# Generating random seed for repeatability, adding version just for the sake of clarity/ repeatability

beta = 0.155
sigma = 1 / 5.2
gamma = 1 / 12.39


nodes= 10000
# population size
"""" DO NOT CHANGE UNLESS YOU WANT TO CHANGE THE PROPORTION OF PEOPLE TITLED SUPERSPREADERS"""
superspreaderProportion = 0.2
generalpopulationProportion = (1 - superspreaderProportion)
# Defining proportions of superspreaders vs general population

superspreaderNumber = int(superspreaderProportion * nodes)
# Number of superspreaders within the population
generalpopulationNumber = int(generalpopulationProportion * nodes)
# Number of 'general population' in the population - i.e. non-superspreaders

""" VACCINE NUMBERS """
# TODO: CHANGE VACCINE BUDGET PROPORTION
VaccineBudgetProportion = 1.0
actualVaccineBudget = int(VaccineBudgetProportion * nodes)
# NOTE: CHANGE THIS IF YOU WANT TO CHANGE VACCINE BUDGET
# ALSO NOTE THAT YOU CAN CHANGE actualVaccineBudget to an arbitrary number


# TODO: CHANGE SUPERSPREADER VACCINE COMPLIANCE
superspreaderVaccineCompliance = 1.0

superspreaderVaccineProportionPop = superspreaderProportion * superspreaderVaccineCompliance
if superspreaderVaccineProportionPop > VaccineBudgetProportion:
    superspreaderVaccineProportionPop = VaccineBudgetProportion


superspreaderVaccinatedNum = int(superspreaderVaccineProportionPop * nodes)
generalpopulationVaccinatedNum = int(actualVaccineBudget - superspreaderVaccinatedNum)
if generalpopulationVaccinatedNum > generalpopulationNumber:
    generalpopulationVaccinatedNum = generalpopulationNumber
# GENERATES THE NUMBER OF PEOPLE VACCINATED IN EACH POPULATION




for i in range(10):
    # load the graph - for all test conditions we want to make sure we have exactly the same graph,
    # that is why we don't generate it randomly every time!
    baseGraph = pickle.load( open('socialgraph_' + str(i), "rb" ) )
    # compute degree distribution for the graph
    degree_individuals = [d for n, d in baseGraph.degree()]
    sorted_degree_sequence = sorted(degree_individuals)
    # degree sequence
    sorted_index_individuals = np.argsort(degree_individuals)
    # divide population in superspreaders and not superspreaders based on their degree (number of contacts)
    superSpreaders = sorted_index_individuals[-superspreaderNumber-1:-1]
    generalPopulation = sorted_index_individuals[:generalpopulationNumber]
    # we set the simulation with initE infected
    model = SEIRSNetworkModel(G=baseGraph, beta=beta, sigma=sigma, gamma=gamma, initE=20, budget='unequal', p_local=0.9, p_global=0.1)
    # model.X stores the state of each individual
    # model = 1 (susceptible), model = 2 (exposed), model = 3 (infected), model = 4 (recovered)
    # initially all X will be susceptible, except initE that will be infected
    # We need to set those to recovered (i.e. vaccinated) using different rates for superspreaders and not superspreaders
    # set and enforce fixed budget of vaccinations
    vaccinatedSuperSpreaders = random.sample(list(superSpreaders), superspreaderVaccinatedNum)
    vaccinatedGeneralPopulation = random.sample(list(generalPopulation), generalpopulationVaccinatedNum)
    for n in vaccinatedSuperSpreaders:
        model.X[[n]] = 4
    for n in vaccinatedGeneralPopulation:
        model.X[[n]] = 4
    # NOT SURE HOW TO ITERATE ONE LIST INTO THE GENERAL POPULATION IN ORDER TO VACCINATE PEOPLE/ SET THEM TO R
    # for loop
    # run it for a number of time steps
    model.run(T=400)
    # save the model
    # TODO: set a different name for the model for every condition run (e.g. _superspreaders20percentvaccinated)
    pickle.dump(model, open('_100percentvaccinebudget100percentsuperspreadercompliance' + str(i), "wb" ) )



