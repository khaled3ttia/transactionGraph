import networkx as nx
import matplotlib.pyplot as plt

with open('trace','r') as trace:
    lines_list = [line.rstrip() for line in trace]

print lines_list

d = {}
variables = {}
DG = nx.DiGraph()
readVariables = {}
for i in range(0,len(lines_list)):
    if (lines_list[i].startswith('begin')):
        currentLine = lines_list[i].split('_')
        nameAndTime = currentLine[1].split(':')
        firstname = nameAndTime[0]
        starttime = nameAndTime[1]


    if (lines_list[i].startswith('write')):
        currentLine = lines_list[i].split('_')
        variable_info = currentLine[1].split(':')
        variable_name = variable_info[0]
        variable_version = variable_info[1]
        if (not variables.has_key(variable_name)):
            variables[variable_name] = []
        variables[variable_name].append((firstname, int(variable_version)))


    if (lines_list[i].startswith('read')):
        currentLine = lines_list[i].split('_')
        variable_info = currentLine[1].split(':')
        variable_name = variable_info[0]
        variable_version = variable_info[1]
        if (not readVariables.has_key(variable_name)):
            readVariables[variable_name] = []
        readVariables[variable_name].append((firstname, int(variable_version)))



    if (lines_list[i].startswith('commit')):
        currentLine = lines_list[i].split('_')
        nameAndTime = currentLine[1].split(':')
        secondname = nameAndTime[0]
        endtime = nameAndTime[1]

        if (firstname == secondname):
            d[firstname] = (int(starttime), int(endtime))

print d
#
#
# print d.keys()
print variables
for x in range(0,len(d.keys())):
    # print d[d.keys()[x]]
    for y in range (x+1, len(d.keys())):
        if (d[d.keys()[x]][0] > d[d.keys()[y]][1]):
            DG.add_edge(d.keys()[y],d.keys()[x])
        if (d[d.keys()[y]][0] > d[d.keys()[x]][1]):
            DG.add_edge(d.keys()[x],d.keys()[y])

#
# for z in range(0, len(lines_list)):
#     if (lines_list[z].startswith('read')):
#         readLine = lines_list[z].split('_')
#
#         readLineTransaction = readLine[0]
#         readLineVariable = readLine[1].split(':')
#         readLineVariableName = readLineVariable[0]
#         readLineVariableVersion = int(readLineVariable[1])
#         if variables.has_key(readLineVariableName):
#             for m in range(0,len(variables[readLineVariableName])):
#                 if variables[readLineVariableName][m][0] != readLine[]

# DG.add_edge('T1', 'T2')
# # DG.add_edge('T2', 'T3')
# DG.add_edge('T1', 'T3')
try:
    print list(nx.find_cycle(DG, orientation='original'))
except:
    print "No cycle found"

print readVariables
nx.draw_networkx(DG)
plt.show()

# DG.add_weighted_edges_from([(1,2,10), (2,3,5), (1,3,5)])
# print list(DG.predecessors(3))
#
# print DG.out_degree(1)
# print DG.out_degree(2)
# print DG.in_degree(3)