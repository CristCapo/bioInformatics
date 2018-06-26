import pandas as pd
import src.JsonManager as JsonManager
from collections import OrderedDict
import src.RegexManager as rm
from functools import reduce
import csv

def getDataFrameFromList(columName, stringList):
    return pd.DataFrame({columName : stringList})


def getDataFrameFromExcel(filename, sheeToParse):
    xl = pd.ExcelFile(filename)
    return xl.parse(sheeToParse)

def getDataFrameFromCsv(filename, head=0):
    return pd.read_csv(filename, header=head)

def DataFrameMerger(DataFrames, ColumnsToMerge):
    return(reduce(lambda left,right: pd.merge(left,right,on=[ColumnsToMerge]), DataFrames))
    


def getMiRNAList():

    result = []

    miRNAList = dataFrame['Detector']

    for element in miRNAList:
        result.append(element[:-7])

    return list(set(result))


def searchForTarget(miRNAName):
    results = resulting['Target Gene'].where(resulting['miRNA'] == miRNAName).dropna()

    #### To Avoid, Check merge
    return list(set(results.values.tolist()))


def parser():

    '''
    Creates the csv and the json
    '''

    dataToWrite = []

    for index, row in dataFrame.iterrows():

        content = OrderedDict(row)

        tmpRes = JsonManager.createData(content)

        dataFrame.at[index,'Detector'] = rm.removeMiRNAIdentifier(dataFrame.at[index, "Detector"])

        dataToWrite.append(tmpRes)

    JsonManager.writeJSON(dataToWrite, file)

    (dataFrame.fillna(0)).to_csv("./data/result.csv", header=None)


def createGeneCsv():

    file = open('./data/resTarget.csv', 'w', newline="")
    writer = csv.writer(file)

    for elementName in miRNAList:
        genes = searchForTarget(elementName)
        genes.insert(0, elementName)
        if len(genes) > 1:
            writer.writerow(genes)

    file.close()

"""
    The following is the main class of the software. It is used to open a dataset written in an excel file
"""

filesPath, file = JsonManager.initPath('results')

# Open DataSet
datasetFilename = filesPath + 'Dati HF-LF_3_6_12 mesi.xlsx'
# Local Section
MirTarBaseFilename = filesPath + 'localDB.xls'
rna22Filename = filesPath + 'rna22_Tradotto.txt'
miRDBFilename = filesPath + 'miRDB_Tradotto.txt'



dataFrame = getDataFrameFromExcel(datasetFilename, 'Sheet1')
dataFrame.loc[:, 'Targets'] = 'Waiting'

MirTarBaseDF = getDataFrameFromExcel(MirTarBaseFilename,'miRTarBase')[['miRNA', 'Target Gene']]
rna22DF = getDataFrameFromCsv(rna22Filename)
#miRDBDF = getDataFromCsv(miRDBFilename)

# Creates a dataframe containing only the miRNA under consideration
miRNAList = getMiRNAList()

# Obtains the data frame including the miRNAs
miRNADf = getDataFrameFromList('miRNA', miRNAList)
TargetSource = pd.concat([MirTarBaseDF, rna22DF])
TargetSource.reset_index()





# Obtains the data frame with the genes and the miRNAs
resulting = pd.merge(TargetSource, miRNADf, how = 'inner', on=['miRNA'])
resulting.drop_duplicates(inplace=True)
resulting.reset_index(inplace=True, drop=True)
print(resulting)



    



