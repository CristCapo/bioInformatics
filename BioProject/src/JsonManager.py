import json, os
import src.RegexManager as rm
from src.Replicated import Replicated


def createData(content):
    """
    This function takes the content of a row in the file excel in order to convert it in JSON format.
    The experiments are created in the dictionary replicateds, in which a key is the couple (ct, duration) (i.e.
    (1, 3m) represents the replicated 1 during the 3m period). To find out which replicated is going to be parsed,
    the RegexManager's functions are used.

    :param content: a dictionary containing the row's content of the Excel file
    :return data: the dictionary that will be used to create the JSON file
    """
    replicateds = {}
    name = rm.removeMiRNAIdentifier(content["Detector"])
    targets = []
    number = 0

    for key in content.keys():
        ct = rm.findReplicatedCtNumber(key)
        rq = rm.findReplicatedRqNumber(key)
        duration = rm.findDuration(key)

        if ct is not None and duration is not None:
            replicateds[(ct, duration)] = Replicated()
            replicateds[(ct, duration)].Number = number
            replicateds[(ct, duration)].CT = str(content[key])
            replicateds[(ct, duration)].Duration = duration
            replicateds[(ct, duration)].Diet = rm.findDiet(content['Sample'])
            number += 1

        if rq is not None and duration is not None:
            if str(content[key]) != 'nan':
                replicateds[(rq, duration)].RQ = str(content[key])

    dictlist = []

    for repl in replicateds:
        dictlist.append({"number": replicateds[repl].Number,
                         "rq": replicateds[repl].RQ,
                         "ct": replicateds[repl].CT,
                         "duration": replicateds[repl].Duration,
                         "diet": replicateds[repl].Diet})

    data = {
        'miRNA': name,
        'targets': targets,
        "replicated": dictlist,
    }

    return data


def writeJSON(data, file):
    file.write(json.dumps(data, indent=2))

def initPath(filename):

    filesPath = os.getcwd() + "/data/"
    filename = filesPath + filename + ".json"
    file = open(filename, 'w')
    return filesPath, file


