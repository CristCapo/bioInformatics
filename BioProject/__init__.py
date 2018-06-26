import os
from src import ExcelParser as ep
#from src import JsonManager as jsm


"""
	the __init.py__ is used to control the flow of the program. It can be divided in:
		1) Get the the .json version of the input dataset 
		2) Search for miRNA in an externalDB and complete the .json file with correspondent genes
		3) Import the .json file in Neo4j for a graph visualization
"""
#filesPath = os.path.dirname(os.getcwd()) + "/data/"
# Phase 1 
ep.parser()
ep.createGeneCsv()

