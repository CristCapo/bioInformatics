import re as re

def findDuration(columnName):

    result = re.search('3m|6m', columnName, flags=re.I)
    try:
        return result.group(0)
    except AttributeError:
        return None

def findReplicatedNumber(columnName):

    result = re.finditer(r'ct.*(1|2|3)|rq.*(1|2|3)', columnName, flags=re.IGNORECASE)
    try:
        for matchNum, match in enumerate(result):

            for groupNum in range(0, len(match.groups())):
                groupNum += 1

                if match.group(groupNum) is not None:
                    return match.group(groupNum)
    except AttributeError:
        return None

def findReplicatedCtNumber(columnName):
    result = re.finditer(r'(ct).*(1|2|3)', columnName, flags=re.IGNORECASE)

    try:
        for matchNum, match in enumerate(result):

            for groupNum in range(0, len(match.groups())):
                groupNum += 1

                if match.group(2) is not None:
                    return match.group(2)
    except AttributeError:
        return None

def findReplicatedRqNumber(columnName):
    result = re.finditer(r'(rq).*(1|2|3)', columnName, flags=re.IGNORECASE)
    try:
        for matchNum, match in enumerate(result):

            for groupNum in range(0, len(match.groups())):
                groupNum += 1

                if match.group(2) is not None:
                    return match.group(2)
    except AttributeError:
        return None

def findDiet(columnName):

    result = re.search(r"lf|hf", columnName, flags=re.IGNORECASE)
    try:
        return result.group(0)
    except AttributeError:
        return None

def removeMiRNAIdentifier(columnName):
    result = re.search(r"(.*)(-[^a-z][0-9]*$)", columnName, flags=re.IGNORECASE)
    return result.group(1)

def findReplicatedName(data):
    result = re.search(r"(\D*)(\d*)(\D*)", data, flags=re.IGNORECASE)
    print("result")
    print(result.group(2))
    try:
        if result.group(1) is "" and result.group(3) is "":
            print("replicated")
            return True
        else:
            print("not replicated")
            return False
    except AttributeError:
        return None