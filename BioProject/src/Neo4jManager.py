from py2neo import Database, Graph, Node, Relationship
import json
import RegexManager as rm
#
# loadResultCSVTransaction = graph.begin(autocommit=True)
#
# queryLoadResultCsv = "USING PERIODIC COMMIT LOAD CSV FROM 'file:///result.csv' AS line\
# MERGE (mi : miRNA { name: line[2]})\
# MERGE (re : replicated { name: line[0]})\
# MERGE (mi)-[:Expressed]->(re)"
#
# loadResultCSVTransaction.run(queryLoadResultCsv)
#
# loadResTargetCSVTransaction = graph.begin(autocommit=True)
#
# queryLoadResTargetCsv = "USING PERIODIC COMMIT \
# LOAD CSV FROM 'file:///resTarget.csv' AS line MATCH(mi:miRNA {name : line[0]})\
# FOREACH(geneName IN line[1..] | \
# MERGE (ge : genes { name: geneName })\
# MERGE (mi)-[:Expressed]->(ge))"
#
# loadResTargetCSVTransaction.run(queryLoadResTargetCsv)


def getResultsFromSite(mirna, ct, rq, gene):

    if ct is None or ct == "":
        #todo
        pass
    if rq is None or ct == "":
        #todo
        pass

    query = "MATCH (n) -[]-> (m) where n.name='" + mirna + "' return n, m"
    dataSet = graph.run(query).data()


    nodesList = []
    linksList = []
    group = 1
    nodesList.append({'id': dataSet[0]['n']['name'], "group": 1})

    for data in dataSet:

        if rm.findReplicatedName(data['m']['name']) == True:
            group = 4
        elif rm.findReplicatedName(data['m']['name']) == False:
            group = 7

        nodesList.append({"id": data['m']['name'], "group": group})
        linksList.append({"source": data['n']['name'], "target": data['m']['name'], "value": 1})

    toWrite = {'nodes': nodesList,
               'links': linksList}

    file = open('sicuramente.json', 'w')

    file.write(json.dumps(toWrite, indent=2))
    print("culo finished")





User = 'neo4j'
Password = 'bioinfo'
graph = Graph(uri='http://localhost', port=7474, auth=(User, Password))

getResultsFromSite("mmu-miR-339-5p", None, None, None)