# -*- coding: utf-8 -*-

import os
import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def create_data():

	# figure 1 data

	x1 = ["République \ntchèque",
		  "Slovakie",
		  "Autriche",
		  "Allemagne",
		  "Italie",
		  "Pays-Bas",
		  "Pologne",
		  "Canada",
		  "Royaume-Uni",
		  "Belgique",
		  "Danemark",
		  "France",
		  "Espagne",
		  "États-Unis",
		  "Japon",
		  "Norvège",
		  "Estonie",
		  "Irlande",
		  "Suède",
		  "Finlande",
		  "Corée du Sud",
		  "Russie"]

	y1a = [44, 44, 43, 43, 43, 40, 40, 39, 39, 38, 38, 38, 38, 38, 37, 37, 36, 36, 36, 35, 35, 29]
	y2a = [9, 10, 11, 11, 9, 9, 6, 8, 9, 6, 8, 8, 12, 8, 6, 9, 5, 7, 6, 6, 5, 2]

	data1 = pd.DataFrame([x1, y1a, y2a])
	data1.to_csv("data/figure1.csv", header=False, index=False)

	# figure 2 data

	x2 = ["Préparation \nde nourriture",
		  "Construction",
		  "Nettoyage",
		  "Conduite",
		  "Agriculture",
		  "Fabrication \nde vêtements",
		  "Services \npersonnels",
		  "Vente",
		  "Service à \nla clientèle",
		  "Administration \ndes affaires",
		  "Technologies \nde l'information",
		  "Sciences et génie",
		  "Santé",
		  #"Gestion de l'hôtellerie \n et de la vente au détail",
		  "Gestion",
		  "Haute direction \net politique",
		  "Enseignement"]

	y2 = [64, 59, 59, 58, 57, 56, 54, 52, 49, 43, 41, 41, 35, 34, 30, 28]

	data2 = pd.DataFrame([x2, y2])
	data2.to_csv("data/figure2.csv", header=False, index=False)

	# figure 3 data

	x3 = ["Primaire \net moins",
		  "Début du \nsecondaire",
		  "Fin du \nsecondaire",
		  "Post-secondaire",
		  "Études \nuniversitaire \nnon complétées",
		  "Baccalauréat",
		  "Maitrise ou \nDoctorat"]

	y3 = [54., 40., 14., 8., 5., 1., 0.5]

	data3 = pd.DataFrame([x3, y3])
	data3.to_csv("data/figure3.csv", header=False, index=False)

def make_figure_1():
	""" 
	Re-creating the Potential of automation figure
	https://www.mastercardcenter.org/insights/end-work-know
	"""
	with open("data/figure1.csv") as data_file:
		data = pd.read_csv(data_file, header=None)

	plt.figure(figsize=(13.5, 9))

	labels = data.iloc[0].values
	vals1 = data.iloc[1].values.astype(float)
	vals2 = data.iloc[2].values.astype(float)

	index = np.arange(len(labels))

	y_index = np.arange(0, max([max(vals1), max(vals2)]) + 5, 5)

	plt.bar(index - 0.15, vals1, width=0.3, label=u"Automatisation moyenne")
	plt.bar(index + 0.15, vals2, width=0.3, label=u"Risque élevé")


	plt.yticks(y_index, [str(s) + "%" for s in y_index], fontsize=18)
	plt.xticks(index, [unicode(s, "utf-8") for s in labels], rotation="vertical", fontsize=18)
	plt.title("Potentiel d'automatisation des emplois, pays de l'OCDE", fontsize=24)
	plt.legend(fancybox=True, fontsize=18)

	plt.tight_layout()
	plt.savefig("figures/figure1.png")

def make_figure_2():
	"""
	Re-creating the Automated for the people figure
	https://www.economist.com/graphic-detail/2018/04/24/a-study-finds-nearly-half-of-jobs-are-vulnerable-to-automation
	"""
	with open("data/figure2.csv") as data_file:
		data = pd.read_csv(data_file, header=None)

	plt.figure(figsize=(11, 7.5))

	labels = data.iloc[0].values
	vals = data.iloc[1].values.astype(float)

	index = np.arange(len(labels)).astype(float)
	y_index = np.arange(0, max(vals) + 5, 10)

	# scale
	index *= 1.1
	plt.bar(index, vals)

	plt.yticks(y_index, [str(s) + "%" for s in y_index], fontsize=18)
	plt.xticks(index, [unicode(s, "utf-8") for s in labels], rotation="vertical", fontsize=16)
	plt.title("Potentiel d'automatisation par type d'emploi", fontsize=24)

	plt.tight_layout()
	plt.savefig("figures/figure2.png")


def make_figure_3():
	"""
	Re-creating the Share of workers with high automatibility by education figure
	https://www.researchgate.net/figure/Share-of-Workers-with-High-Automatibility-by-Education_fig6_303311529
	"""
	with open("data/figure3.csv") as data_file:
		data = pd.read_csv(data_file, header=None)

	plt.figure(figsize=(11, 7.5))

	labels = data.iloc[0].values
	vals = data.iloc[1].values.astype(float)

	index = np.arange(len(labels)).astype(float)
	y_index = np.arange(0, max(vals) + 5, 10)

	plt.bar(index, vals)

	plt.yticks(y_index, [str(s) + "%" for s in y_index], fontsize=18)
	plt.xticks(index, [unicode(s, "utf-8") for s in labels], rotation="vertical", fontsize=16)
	plt.title(u"Proportion des travailleurs à risque élevé (>70%) \nd'automatisation par niveau d'éducation", fontsize=24)

	plt.tight_layout()
	plt.savefig("figures/figure3.png")
if __name__ == "__main__":

	create_data()

	make_figure_1()

	make_figure_2()

	make_figure_3()

