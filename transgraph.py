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
        variables[variable_name][firstname] = int(variable_version)
        # variables[variable_name].append((firstname, int(variable_version)))
    if (lines_list[i].startswith('read')):
        variable_info = currentLine[1].split(':')
        variable_name = variable_info[0]
        variable_version = variable_info[1]
        if (not readVariables.has_key(variable_name)):
            readVariables[variable_name] = {}
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
            DG.add_edge(d.keys()[y],d.keys()[x], lbl='x')
        if (d[d.keys()[y]][0] > d[d.keys()[x]][1]):
            DG.add_edge(d.keys()[x],d.keys()[y], lbl='y')
try:
    print list(nx.find_cycle(DG, orientation='original'))
except:
    print "No cycle found"



# for key,value in variables.iteritems():
#     for k,v in readVariables.iteritems():
#         if k==key:
#             for i in range(0,len(v)):
#                 if v[i]

# pos = nx.spring_layout(DG)
#
# nx.draw_networkx(DG,pos, node_size=2000)
#
#
# edge_labels=dict([((u,v,),d['lbl'])
#              for u,v,d in DG.edges(data=True)])
# nx.draw_networkx_edge_labels(DG, pos, edge_labels=edge_labels)

print variables
print readVariables
# plt.show()

