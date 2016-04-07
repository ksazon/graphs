import matplotlib.pyplot as plt
import networkx as nx
from string import ascii_uppercase
# nonsens


def graphInput():
    while True:
        nodesPair = raw_input(": ")
        if nodesPair[0] == '0':
            degreesPrint()
            graphics()
            break
        nodesPair = nodesPair.upper()
        print (nodesPair)
        assert nodesPair[0] and nodesPair[1] in G.nodes(), \
            "Podaj wierzcholki z zakresu podanego powyzej"
        G.add_edge(*nodesPair)
        degree(nodesPair)


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
    nx.draw_networkx_nodes(G, pos, node_size=700)
    # edges
    nx.draw_networkx_edges(G, pos, width=6)
    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
    plt.axis('off')
    # save as png
    plt.savefig("graf.png")
    # plt.show()


def nodesEven():
    ans = True
    for n in G.nodes():
        if G.node[n] % 2 == 1:
            ans = False
            break
    if ans is False:
        print "********************"
        print "Istnieja nieparzyste wierzcholki - nie jest to graf Eulerowski"
        print "********************"
    else:
        connectedGraph()


def DFSVisit(node):
    for innerNode in G.neighbors(node):
        # print "2", innerNode
        # print "wizy: ", visited
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
    G.node[i] = 0

print "Wierzchoki to:\n", sorted(G.nodes())
print "Podaj miedzy ktorymi wierzcholkami istnieje krawedz (np. ac)"
print "Po wprowadzeniu wszystkich wprowadz 0, enter\n"

graphInput()
nodesEven()
