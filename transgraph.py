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
            variables[variable_name] = {}
        # if (not variables[variable_name].has_key(firstname)):
        #     variables[variable_name][firstname] = []
        # variables[variable_name][firstname].append(int(variable_version))
        variables[variable_name][firstname] = int(variable_version)

    if (lines_list[i].startswith('read')):
        variable_info = currentLine[1].split(':')
        variable_name = variable_info[0]
        variable_version = variable_info[1]
        if (not readVariables.has_key(variable_name)):
            readVariables[variable_name] = {}
        # if (not readVariables[variable_name].has_key(firstname)):
        #     readVariables[variable_name][firstname] = []
        # readVariables[variable_name][firstname].append(int(variable_version))
        readVariables[variable_name][firstname] = int(variable_version)

        # readVariables[variable_name].append((firstname, int(variable_version)))
    if (lines_list[i].startswith('commit')):
        nameAndTime = currentLine[1].split(':')
        secondname = nameAndTime[0]
        endtime = nameAndTime[1]
        if (firstname == secondname):
            d[firstname] = (int(starttime), int(endtime))


print d
for x in range(0,len(d.keys())):
    for y in range (x+1, len(d.keys())):
        if (d[d.keys()[x]][0] > d[d.keys()[y]][1]):
            DG.add_edge(d.keys()[y],d.keys()[x],lbl='', color='g',width=2)
        if (d[d.keys()[y]][0] > d[d.keys()[x]][1]):
            DG.add_edge(d.keys()[x],d.keys()[y],lbl='', color='g',width=2)
try:
    print list(nx.find_cycle(DG, orientation='original'))
except:
    print "No cycle found"

for key,value in readVariables.iteritems():
    if variables.has_key(key):
        entry = variables[key]
        entry2 = readVariables[key]
        for k,v in entry.iteritems():
            for k1,v1 in entry2.iteritems():
                if v == v1:
                    if (DG.has_edge(k,k1)):
                        DG.add_edge(k, k1,lbl=key, color='b', width=2)
                    else:
                        DG.add_edge(k, k1, lbl="ERR! " + key, color='r', width=2)
                        print "Real-time order violation: " + str(k1) + " reads verison " + str(v) + " of variable " + str(key) + " from the wrong transaction " + str(k)
                    # DG.add_edge(k,k1,lbl=key)
# for key,value in variables.iteritems():
#     for k,v in readVariables.iteritems():
#         if k==key:
#             for i in range(0,len(v)):
#                 if v[i]

try:
    print list(nx.find_cycle(DG, orientation='original'))
except:
    print "No cycle found"


pos = nx.spring_layout(DG)
#
nx.draw_networkx(DG,pos, node_size=600)
#
#
colors = [DG[u][v]['color'] for u,v in DG.edges()]
weights = [DG[u][v]['width'] for u,v in DG.edges()]
edge_labels=dict([((u,v,),d['lbl'])
             for u,v,d in DG.edges(data=True)])
nx.draw_networkx_edge_labels(DG, pos, edge_labels=edge_labels, font_size=12)
nx.draw_networkx_edges(DG, pos, edge_color=colors, width=weights, arrowsize=3, alpha=0.5)
print variables
print readVariables
#plt.show()
plt.savefig('outputGraph.png')
