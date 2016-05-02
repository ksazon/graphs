import matplotlib.pyplot as plt
# from matplotlib.pyplot import cm
import networkx as nx
# import operator
from string import ascii_uppercase
# nonsens


def graphInput():
    while True:
        nodesPair = raw_input(": ")
        if nodesPair[0] == '0':
            degreesPrint()
            # graphics()
            break
        nodesPair = nodesPair.upper()
        print (nodesPair)
        assert nodesPair[0] and nodesPair[1] in G.nodes(), \
            "Podaj wierzcholki z zakresu podanego powyzej"
        G.add_edge(*nodesPair)
        degree(nodesPair)


def dummy():
    G.add_edge('A', 'B')
    G.add_edge('B', 'C')
    G.add_edge('C', 'D')
    G.add_edge('D', 'E')
    G.add_edge('E', 'A')
    G.add_edge('F', 'A')
    G.add_edge('F', 'B')
    G.add_edge('F', 'C')
    G.add_edge('F', 'D')
    G.add_edge('F', 'E')
    G.node['A']['deg'] = 3
    G.node['B']['deg'] = 3
    G.node['C']['deg'] = 3
    G.node['D']['deg'] = 3
    G.node['E']['deg'] = 3
    G.node['F']['deg'] = 5

    coloring()
    graphics()


def degree(nodesPair):
    nodeName = nodesPair[0]
    G.node[nodeName] += 1
    nodeName = nodesPair[1]
    G.node[nodeName] += 1


def degreesPrint():
    degrees = []
    # print "\nStopnie wierzcholkow to:"
    for node in sorted(G.nodes()):
        # print "deg(", node, ")", " = ", G.node[node]
        degrees.append(G.node[node])
    # print "\nJest to graf", max(degrees), "stopnia"


def graphics():
    # positions for all nodes
    pos = nx.spring_layout(G)
    # nodes
    #color=iter(cm.rainbow(np.linspace(0,1,n)))
    for c in ['r', 'b', 'g', 'k', 'm']:
        nx.draw_networkx_nodes(G, pos, node_color=c, node_size=700)
    # edges
    nx.draw_networkx_edges(G, pos, width=6)
    labels = {}
    for node in G.nodes():
        labels[0] = r'G.node[iNode]['color']'
        nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
    plt.axis('off')
    # save as png
    plt.savefig("graf.png")
    plt.show()


def nodesEven():
    # ans = True
    unbillicalCount = 0
    for n in G.nodes():
        if G.node[n] % 2 == 1:
            unbillicalCount += 1
    if unbillicalCount != 2 and unbillicalCount != 0:
        print "********************"
        print "Ilosc nieparzystych wierzcholkow nie jest rowna 0 ani 2, nie jest to graf Eulerowski ani poleulerowski"
        print "********************"
    else:
        connectedGraph()
        if unbillicalCount == 2:
            print "Poleulerowski"


def DFSVisit(node):
    for innerNode in G.neighbors(node):
        # print "2", innerNode
        # print "wizy: ", visited
        # print "odwiedzany teraz:
        if innerNode not in visited:
            visited.append(innerNode)
            DFSVisit(innerNode)


def connectedGraph():
    visited.append('A')
    DFSVisit('A')

    ans = 0
    for letter in G.nodes():
        if letter not in visited:
            ans = 1
            break
    if ans == 0:
        print "********************"
        print "Jest to piekny graf - Eulerowski"
        print "********************"
    else:
        print "********************"
        print "Graf nie jest spojny - nie jest to graf Eulerowski"
        print "********************"


def coloring():
    # H = nx.Graph()
    # H = G
    for i in G.nodes():
        G.node[i]['color'] = -1
        # value for (key, value) in sorted(numbers.items())
    for i in G.nodes():
        print G.node[i]['color']
    # G.node['C']['color'] = 4

    print "g.nodes()", G.nodes()
    print "g", G
    print "g.nodesdata", G.nodes(data=True)
    for node in sorted(G.nodes(data=True), key=lambda n: n[1]['deg'], reverse=True):
        iNode = node[0]
        # print "gino", G.node[node][0], G.node[node][1]['deg']
        neighborsColors = []
        for iiNode in G.neighbors(iNode):
            neighborsColors.append(G.node[iiNode]['color'])
            # print iNode, G.node[iNode][]
        print neighborsColors
        for i in range(G.number_of_nodes()):
            if i not in neighborsColors:
                G.node[iNode]['color'] = i
                break

        print "inode = ", iNode, " i = ", i, "g neib = ", G.neighbors(iNode)



        # for moreInnerNode in H.neighbors(innerNode):
        #     if H.node[innerNode] <= H.node[moreInnerNode]:
        #         H.node[innerNode] = H.node[moreInnerNode] + 1

    for iNode in sorted(G.nodes()):
        print iNode, " = ", G.node[iNode]['color']


global nodesNum
nodesNum = int(raw_input("Podaj ilosc wierzcholkow: "))
assert nodesNum > 1, "Podaj liczbe wieksza od 1"

letters = []
for i in range(nodesNum):
    letter = ascii_uppercase[i]
    letters.append(letter)

global G
global visited
visited = []
G = nx.Graph()
G.add_nodes_from(letters)
for i in G.nodes():
    G.node[i]['deg'] = 0
    # print G.node[i]

print "Wierzchoki to:\n", sorted(G.nodes())
print "Podaj miedzy ktorymi wierzcholkami istnieje krawedz (np. ac)"
print "Po wprowadzeniu wszystkich wprowadz 0, enter\n"

# graphInput()
dummy()
# nodesEven()
# print nx.is_eulerian(G)
