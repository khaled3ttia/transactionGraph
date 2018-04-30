import networkx as nx
import matplotlib.pyplot as plt

with open('trace','r') as trace:
    lines_list = [line.rstrip() for line in trace]

d = {}
variables = {}
DG = nx.DiGraph()
readVariables = {}
for i in range(0,len(lines_list)):
    currentLine = lines_list[i].split('_')
    if (lines_list[i].startswith('begin')):
        nameAndTime = currentLine[1].split(':')
        firstname = nameAndTime[0]
        starttime = nameAndTime[1]
    if (lines_list[i].startswith('write')):
        variable_info = currentLine[1].split(':')
        variable_name = variable_info[0]
        variable_version = variable_info[1]
        if (not variables.has_key(variable_name)):
            variables[variable_name] = []
        variables[variable_name].append((firstname, int(variable_version)))
    if (lines_list[i].startswith('read')):
        variable_info = currentLine[1].split(':')
        variable_name = variable_info[0]
        variable_version = variable_info[1]
        if (not readVariables.has_key(variable_name)):
            readVariables[variable_name] = []
        readVariables[variable_name].append((firstname, int(variable_version)))
    if (lines_list[i].startswith('commit')):
        nameAndTime = currentLine[1].split(':')
        secondname = nameAndTime[0]
        endtime = nameAndTime[1]
        if (firstname == secondname):
            d[firstname] = (int(starttime), int(endtime))
for x in range(0,len(d.keys())):
    for y in range (x+1, len(d.keys())):
        if (d[d.keys()[x]][0] > d[d.keys()[y]][1]):
            DG.add_edge(d.keys()[y],d.keys()[x])
        if (d[d.keys()[y]][0] > d[d.keys()[x]][1]):
            DG.add_edge(d.keys()[x],d.keys()[y])
try:
    print list(nx.find_cycle(DG, orientation='original'))
except:
    print "No cycle found"


nx.draw_networkx(DG)
plt.show()

