import matplotlib.pyplot as plt
import networkx as nx
from string import ascii_uppercase


def degree(nodesPair):
    nodeName = nodesPair[0]
    G.node[nodeName] += 1
    nodeName = nodesPair[1]
    G.node[nodeName] += 1
    # return G


def degreesPrint():
    degrees = []
    print "Stopnie wierzcholkow to:"
    for node in sorted(G.nodes()):
        print "deg(", node, ")", " = ", G.node[node]
        degrees.append(G.node[node])
    print "Jest to graf", max(degrees), "stopnia"
    # return G


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
    plt.savefig("graph.png")
    plt.show()


global nodesNum
nodesNum = int(raw_input("Podaj ilosc wierzcholkow: "))
assert nodesNum > 1, "Podaj liczbe wieksza od 1"

letters = []
for i in range(nodesNum):
    letter = ascii_uppercase[i]
    letters.append(letter)

global G
G = nx.Graph()
G.add_nodes_from(letters)
for i in G.nodes():
    G.node[i] = 0

print "Wierzchoki to: ", sorted(G.nodes())
print "Podaj miedzy ktorymi wierzcholkami istnieje krawedz (np. ac)"
print "Po wprowadzeniu wszystkich wprowadz 0, enter"

while True:
    nodesPair = raw_input(": ")
    if nodesPair[0] == '0':
        degreesPrint()
        break
    nodesPair = nodesPair.upper()
    print nodesPair
    G.add_edge(*nodesPair)
    degree(nodesPair)