import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations

#create gragh
class Graph():

    def __init__(self, agents):
        #Create empty graph
        self.graph = nx.Graph()

        #Add nodes (which are our agents)
        self.graph.add_nodes_from(agents)

        #Add edges - completely connected graph
        edges = combinations(agents, 2)
        self.graph.add_edges_from(edges)

        self.drawGraph()

    def drawGraph(self):
        #Colours - support up to 7 colours at a time
        #Using https://www.cssportal.com/html-colors/x11-colors.php
        colours = ['pink', 'violet', 'limegreen', 'DeepSkyBlue', 'Gold', 'MediumPurple', 'MediumSeaGreen']
        colour_map = []
        for node in self.graph:
            colour_map.append(colours[node.colour])

        #Draw the graph and save to file
        nx.draw(self.graph, node_color=colour_map, width=0.25)
        plt.savefig("graph.png")

    #After a agent has changed state and has a new colour / weight, we need to update the graph
    def updateGraph(self):
        return
