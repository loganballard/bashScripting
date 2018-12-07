import os
import json
from pprint import pprint

SEVERITIES = ['high', 'critical']

def checkSev(sev):
    if sev in SEVERITIES:
        return True
    return False

def getRelevantInfo(fileJson, filename):
    relevance = {}
    fileDict = json.load(fileJson)
    if ('advisories' not in fileDict):
        return None
    relevance['name'] = filename.split('.')[0]
    relevance['actions'] = []
    for adv in fileDict['advisories']:
        advisory = fileDict['advisories'][adv]
        if checkSev(advisory['severity']):
            action = {}
            action['severity'] = 'high'
            action['recommendation'] = advisory['recommendation']
            action['paths'] = []
            for find in advisory['findings']:
                for path in find['paths']:
                    action['paths'].append(path)
            relevance['actions'].append(action)
    if len(relevance['actions']) == 0:
        return None
    return relevance
    
bigOutput = []
for filename in os.listdir('output-jsons'):
    if filename.endswith('.json'):
        path = 'output-jsons/'+filename
        fp = open(path,'r')
        output = getRelevantInfo(fp, filename)
        if output is not None:
            bigOutput.append(output)
        fp.close()
f = open('recommendations.json', 'w+')
json.dump(bigOutput, f)
f.close()