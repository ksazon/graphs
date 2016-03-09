import matplotlib.pyplot as plt
import networkx as nx
from string import ascii_uppercase

global nodesNum
nodesNum = int(raw_input("Podaj ilosc wierzcholkow: "))

assert nodesNum > 1, "Podaj liczbe wieksza od 1"


def degree(nodesPair):
    if nodesPair == ['0', '0']:
        degrees = []
        print "Stopnie wierzcholkow to:"
        for node in sorted(H.nodes()):
            print "deg(", node, ")", " = ", H.node[node]
            degrees.append(H.node[node])
        print "Jest to graf ", max(degrees), "stopnia"
        return H
    nodeName = nodesPair[0]
    H.node[nodeName] += 1
    nodeName = nodesPair[1]
    H.node[nodeName] += 1
    return H

letters = []
G = nx.Graph()
global H

for i in range(nodesNum):
    letter = ascii_uppercase[i]
    letters.append(letter)

G.add_nodes_from(letters)
H = G.copy()
for i in H.nodes():
    H.node[i] = 0

print "Wierzchoki to: ", G.nodes()

print "Podaj miedzy ktorymi wierzcholkami istnieje krawedz (po 1 wierzcholku)"
print "Po wprowadzeniu wszystkich wprowadz 0, enter"
nodesChar = "a"
while True:
    nodesPair = ['a', 'a']
    nodesChar = raw_input("Miedzy wierzcholkiem: ")
    if nodesChar == '0':
        degree(['0', '0'])
        break
    nodesPair[0] = nodesChar.upper()
    nodesChar = raw_input("oraz: ")
    nodesPair[1] = nodesChar.upper()
    print nodesPair
    G.add_edge(*nodesPair)
    degree(nodesPair)

print(G.nodes())
print(G.edges())

pos = nx.spring_layout(G)  # positions for all nodes

# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
nx.draw_networkx_edges(G, pos, width=6)

nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

plt.axis('off')
plt.savefig("graph.png")  # save as png
plt.show()
