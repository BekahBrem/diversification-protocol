#All the imports from our other files
import networkx as nx
from graph import Graph
import time
import random

class Simulation:
    #First thing that happens when we start the simulation
    def __init__(self, graphType, agents, colours, weightsDict, createDrawing):
        """Get the user input to run our simulation with"""
        self.createDrawing = createDrawing
        #self.user_input_obj = UserParameters() #UserInput()
        #self.values = self.user_input_obj.onCall()

        #Values from user input are sent back from a list of the form [int, int, dict]
        #Index 0 is the number of agents
        self.numOfAgents = agents
        #Index 1 is the number of Colours
        self.numOfColours = colours
        #Index 2 is the dictionary of colours and their weights
        self.weights = weightsDict

        self.totalWeights = 0
        for weight in self.weights.values():
            self.totalWeights += weight

        self.agents = self.createAgentsTest()
        self.network = Graph(graphType, self.agents, self.numOfColours, createDrawing)

        #Assign edges and nodes to variables
        self.nodes = self.network.graph.nodes(data=True)
        self.edges = self.network.graph.edges

    def getAgents(self):
        return self.agents

    def getNodes(self):
        return self.nodes

    def getNetwork(self):
        return self.network

    def findNumberInGraph(self, colourIndex):
        count = 0
        for node in self.nodes:
            if node[1]["colour"] == colourIndex:
                count += 1
        return count

    #Returns a list of edges shared with the node passed in as a parameter
    def getSharedEdges(self, sampledNodeId):
        #Create a list of nodes that share an edge with our sampled node
        sharedEdges = []
        for edgeTuple in self.network.graph.edges:
            if sampledNodeId in edgeTuple:
                if sampledNodeId == edgeTuple[0]:
                    sharedEdges.append(edgeTuple[1])
                else: 
                    sharedEdges.append(edgeTuple[0])
        return sharedEdges

    #Samples a node that will be observed by the sampled node.
    def getObservedNode(self, sampledNodeId, sharedEdges):
        #Sample the second node (the one we do the protocol with)
        observedNodeId = sampledNodeId
        observedNode = self.nodes[sampledNodeId]
        #Loop to ensure we don't sample the same node
        found = False
        while (not found):
            observedNodeId = random.randrange(0, len(self.nodes))
            #Check to see if this sample node shares an edge with our first one
            if (observedNodeId in sharedEdges):
                if (observedNodeId == sampledNodeId):
                    observedNodeId = random.randrange(0, len(self.nodes))
                observedNode = self.nodes[observedNodeId]
                found = True
       
        return (observedNode, observedNodeId)

    def step(self, graphNum):
        #Simulates a step of the protocol
        #Sample a node randomly
        sampledNodeId = random.randrange(0, len(self.nodes))
        sampledNode = self.nodes[sampledNodeId]
        
        #Find what other nodes the sampled node shares an edge with
        sharedEdges = self.getSharedEdges(sampledNodeId)

        #Sample a second node for the first node to observe
        observedNodeTuple = self.getObservedNode(sampledNodeId, sharedEdges)
        observedNode = observedNodeTuple[0]

        #Now that we've sampled 2 nodes, we can apply the protocol to them
        #Our first sampled node is the only one that will change state, as this protocol uses the observer model
        sampledColour = sampledNode["colour"]
        sampledShade = sampledNode["shade"]

        observedColour = observedNode["colour"]
        observedShade = observedNode["shade"]

        """Note to readers: Print statements were commented out but not removed from the following
        code in case you wish to uncomment them and follow the behaviour of the protocol in the command
        line"""

        #print("Node " + str(sampledNodeId) + " sampled node " + str(observedNodeTuple[1]))
       
        #Condition 1 (1)
        #If the confidence of observer node is 0 and other node is confident (shade == 1), 
        if (sampledShade == 0 and observedShade == 1):
            #print("Condition 1: shades are different, colour will be changed")
            self.network.graph.nodes[sampledNodeId]["colour"] = observedColour
            self.network.graph.nodes[sampledNodeId]["shade"] = 1
            if(self.createDrawing):
                self.network.updateGraph(graphNum, self.nodes, self.edges)
        #Condition 2
        #If both nodes have the same colour and shade is 1, change shade to 0 w/ probability 1/(weight of colour)
        elif ((sampledColour == observedColour) and (sampledShade == observedShade) and (sampledShade == 1)):
            #print("Condition 2: colour the same and shade == 1 for u and v")
            #Change to light w/ probability 1/(weight of the colour)
            if random.random() < (1/self.weights[sampledColour]): #/(self.totalWeights)
                sampledShade = 0
                #print("- shade was changed")
                self.network.graph.nodes[sampledNodeId]["shade"] = 0
                if(self.createDrawing):
                    self.network.updateGraph(graphNum, self.nodes, self.edges)
        #If we don't meet the 2 conditions above, don't change anything
        else: 
            #print("Condition 3: no change")
            pass

    #Performs the number of steps of the protocol provided as an argument
    def performSteps(self, steps):
        for stepNum in range(steps):
            self.step(stepNum)
    
    #Creates a list of agents that are used to generate the graph of nodes
    def createAgentsTest(self):
        agentsList = []
        idCounter = 0
        for colour in range(self.numOfColours):
            #First requirement (sustainability): Agent of every colour
            #Shade of every colour is initially 1 (dark)
            agentsList.append((idCounter, {"colour": colour, "shade": 1}))
            idCounter += 1

        #Now, we can create all the other agents with a randomly chosen colour !!! VERSION 1 !!!
        #To find how many remaining agents we have to create we taken number of agents - number of colours
        for agents in range(self.numOfAgents - self.numOfColours):
            #Randomly generate a number between 0 & number of colours
            agentsList.append((idCounter, {"colour": random.randrange(0, self.numOfColours), "shade": 1}))
            idCounter += 1

        return agentsList

