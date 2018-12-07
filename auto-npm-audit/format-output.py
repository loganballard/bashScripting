import json
import os

prefix = "After running a security scan, it was determined that one or more risks are present in this repo."

def makeTicket(info):
    ticket = prefix + "\n\n"
    ticket = ticket + "In the "+info['name']+" repo, these actions should be taken:\n\n"
    for action in info['actions']:
        ticket = ticket + "Problematic Module: "+action['module'] + "\n\n"
        ticket = ticket + "\tSeverity: "+action['severity']+"\n"
        ticket = ticket + "\tRecommendation: " + action['recommendation']+"\n"
        ticket = ticket + "\tPath(s):\n"
        for path in action['paths']:
            ticket = ticket + "\t\t"+path.replace(">", " -> ")+"\n"
        ticket = ticket + "\n"
    return ticket

recJson = json.load(open("recommendations.json", "r"))

for vulner in recJson:
    ticketFile = "./tickets/" + vulner['name']
    ticket = makeTicket(vulner)
    fp = open(ticketFile, 'w+')
    fp.write(ticket)
    fp.close()