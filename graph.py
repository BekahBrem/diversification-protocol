import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations
import random
import numpy as np

#create graph
class Graph():

    graph = []

    def __init__(self, agents, numColours, createDrawing):
        #Create empty graph
        self.seed=32
        self.graph = nx.Graph()
        self.numColours = numColours

        #Add nodes (which are our agents)
        self.graph.add_nodes_from(agents)
        
        #Add edges - completely connected graph
        ids = []
        for thisId in self.graph.nodes:
            ids.append(thisId)

        #edges = combinations(ids, 2)
        edges = self.createCycle(ids)

        self.graph.add_edges_from(edges)

        if (createDrawing):
            #Draw the graph
            self.drawGraph(1)

        graph = self.graph

    def createConnected(self, ids):
        edges = []
        edges = combinations(ids, 2)
        return edges

    def createCycle(self, ids):
        edges = []
        for nodeId in ids:
            if (nodeId+1 in ids):
                edges.append((nodeId, nodeId+1))
            else:
                edges.append((nodeId, 0))
        return edges

    #Assign colours to nodes
    def assignColours(self):
        #For each colour put into an array
        colours = []
        for node in self.graph.nodes(data=True):
            colours.append(node[1].get("colour"))
        return colours

    #Assign sizes to nodes that correspond with the shade (confidence) of that node
    def assignShades(self):
        node_sizes = []
        for node in self.graph.nodes(data=True):
            if node[1].get("shade") == 1:
                node_sizes.append(500)
            else:
                node_sizes.append(200)
        return node_sizes


    #Draws the graph & saves to a file to display later
    def drawGraph(self, id):
        self.fig = plt.figure()
        
        #Give visual representation of colour and confidence of each node
        colours = self.assignColours()
        sizes = self.assignShades()
       
        #Create a legend of all the colours using the same colourmap & normalise for the number of colours
        sm = plt.cm.ScalarMappable(cmap=plt.cm.plasma, norm=plt.Normalize(vmin = 0, vmax=self.numColours))
        ax = self.fig.add_subplot(1,1,1)
        cols = list(range(0, self.numColours))
        for label in cols:
            ax.plot([0],[0], color = sm.to_rgba(label), label = "Colour " + str(label))

        #Draw the graph and save to file
        #Use a seed to produce layout which we then reuse to make it more readable
        my_pos = nx.spring_layout(self.graph, seed = 100)
        
        nx.draw(self.graph, pos = my_pos, node_color=colours, cmap=plt.cm.plasma, vmin=0, vmax= self.numColours, width=0.25, with_labels=True, node_size=sizes)
        
        #Create the legend out of the labels we defined earlier
        plt.legend()
        
        #Save the graph as a png
        plt.savefig("graph" + ".png")
        self.previousGraph = self.graph

    #Updates the graph
    def updateGraph(self, graphNum, nodes, edges):
        #Clear the figure otherwise it will write over it
        self.fig.clear()

        #Add nodes to the graph from generated agents
        self.graph.add_nodes_from(nodes)
        
        #Add edges - completely connected graph
        ids = []
        for thisId in self.graph.nodes:
            ids.append(thisId)

        edges = self.createCycle(ids)
        #edges = combinations(ids, 2)
        self.graph.add_edges_from(edges)

        #Redraw the graph
        self.drawGraph(graphNum)



