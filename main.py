#All the imports from our other files
import networkx as nx
from agent import Agent
from graph import Graph
import scheduler
from  userInput import UserInput
import random

class Storage:
    def __init__(self, colours, weights):
        self.colours = colours
        self.weights = weights

class Simulation:
    #First thing that happens when we start the simulation
    def __init__(self):
        """Get the user input to run our simulation with"""
        self.user_input_obj = UserInput()
        self.values = self.user_input_obj.onCall()
        print("values: ", self.values)
        #Values from user input are sent back from a list of the form [int, int, dict]
        #Index 0 is the number of agents
        self.numOfAgents = self.values[0]
        #Index 1 is the number of Colours
        self.numOfColours = self.values[1]
        #Index 2 is the dictionary of colours and their weights
        self.weights = self.values[2]

        print("values: ", self.values)

        self.agents = self.createAgents()
        self.network = Graph(self.agents)

        storage = Storage(self.numOfColours, self.weights)


    #One of the first things we need to do is create agents
    def createAgents(self):
        #We will put these agents into a graph, first we need to create them all according to the requirements of the protocol
        agentsList = []
        idCounter = 0
        #Firstly, we need to ensure we have at least one agent of every colour
        for colour in range(self.numOfColours):
            #First requirement (sustainability): Agent of every colour
            #Shade of every colour is initially 1 (dark)
            agent = Agent(colour, 1, idCounter)
            agentsList.append(agent)
            idCounter += 1

        #Now, we can create all the other agents with a randomly chosen colour !!! VERSION 1 !!!
        #To find how many remaining agents we have to create we taken number of agents - number of colours
        for agents in range(self.numOfAgents - self.numOfColours):
            #Randomly generate a number between 0 & number of colours
            agent = Agent(random.randrange(0, self.numOfColours), 1, idCounter)
            agentsList.append(agent)
            idCounter += 1

        return agentsList

    

#Run simulation
Simulation()
