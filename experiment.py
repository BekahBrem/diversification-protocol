import networkx as nx
from agent import Agent
from graph import Graph
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from main import Simulation
import math 
import matplotlib.pyplot as plt
import numpy as np

#By Binod Bhattarai, found on: https://github.com/binodbhttr/mycolorpy
from mycolorpy import colorlist as mcp


class Experiment():

    def displayInputTable(self):
        #Create table
        columns=('Number of Agents', 'Number of Colours', 'Total of Weights', 'Result Accuracy')
        tree = ttk.Treeview(self.output, columns=columns, show='headings', height=3)
        for column in columns:
            tree.column(column, anchor=CENTER)  
            tree.heading(column, text=column)  

        tree.grid(row=1, column=0, sticky = "NESW", columnspan=2)
        accuracy = self.calculateAccuracy(self.results)
        tree.insert("", "end", values=(self.numOfAgents, self.numOfColours, self.getTotalWeight(), accuracy))

    def getProportionWeight(self, colour):
        total = self.getTotalWeight()
        proportion = self.weights[colour]/total
        return round((proportion*100), 2)

    def getTotalWeight(self):
        totalWeights = 0
        for weight in self.weights.values():
            totalWeights += weight
        return totalWeights

    def calculateColourRepresentation(self, colour):
        colourCount = self.simulation.findNumberInGraph(int(colour))
        return colourCount

    #Calculate how many nodes of a colour are expected to be in the graph at covergence
    def calculateExpectedNodes(self, colour):
        expectedNodes = (self.weights[colour] * self.numOfAgents) / self.getTotalWeight()
        if (math.floor(expectedNodes) == 0):
            return 1
        else:
            return math.floor(expectedNodes)

    def displayWeightTable(self):
        #Create table
        columns=('Colour (ID)', 'Weight', '# Nodes Expected')
        tree = ttk.Treeview(self.output, columns=columns, show='headings', height=3)
        for column in columns:
            tree.column(column, anchor=CENTER) 
            tree.heading(column, text=column)    

        tree.grid(row=3, column=0, sticky = "NESW", columnspan=2)

        temp = list(range(0, self.numOfColours))
        for colour in temp:
            currentNodes = self.calculateColourRepresentation(colour)
            tree.insert("", "end", values=(colour, self.weights[colour], self.calculateExpectedNodes(colour)))

        #Scrollbar for table
        #Solution was found on: https://stackoverflow.com/questions/39707184/how-to-get-an-all-sticky-grid-of-treeview-and-scrollbar-in-python-tkinter
        #Solution by: Bryan Oakley, Sep 26, 2016 at 16:20, profile: https://stackoverflow.com/users/7432/bryan-oakley
        yscrollbar = ttk.Scrollbar(self.output, orient='vertical', command = tree.yview)
        tree.configure(yscrollcommand = yscrollbar.set)
        yscrollbar.grid(row=3, column=3, sticky='nse')
        yscrollbar.configure(command=tree.yview)

    def doSteps(self, expectedSteps):
        for step in range(0, (math.floor((expectedSteps))+500), 25):
            self.simulation.performSteps(10)
            for colour in range(self.numOfColours):
                count = self.calculateColourRepresentation(colour)
                if(step == 0):
                    self.y_values[colour] = [count]
                else:
                    self.y_values[colour].append(count)
            self.x_values.append(step)


    def calculateAccuracy(self, experimentsList):
        runningSumPercentageErrors = {}
        for experiment in experimentsList:
            listExperimentAccuracies = {}
            
            for colour in experiment:
                expected = self.calculateExpectedNodes(colour)
                actual = experiment[colour]
                accuracy = (abs(expected-actual) / expected)
                listExperimentAccuracies[colour] = accuracy

            for value in listExperimentAccuracies.keys():
                try:
                    runningSumPercentageErrors[value] = runningSumPercentageErrors[value] + listExperimentAccuracies[value]
                except:
                    runningSumPercentageErrors[value] = listExperimentAccuracies[value]

        errorsTotal = 0
        for error in runningSumPercentageErrors.values():
            errorsTotal += 1
        
        #print(100 - errorsTotal)
        return 100 - errorsTotal

    def createGraphNodesOverTime(self):
        #Create graphs of the colours of nodes over time
        #Data required to do this: dict of colours & num of nodes at each timestep
        self.fig = plt.figure()

        colormap=mcp.gen_color(cmap="plasma", n=self.numOfColours)

        #Get colour at each step
        for colour in range(self.numOfColours):
            #plot(x,y)
            label = 'Colour: ' + str(colour) + ", Weight: " + str(self.weights[colour])
            plt.plot(self.x_values, self.y_values[colour], color=colormap[colour], label=label)

        for colour in range(self.numOfColours):
            listConvergence = [self.calculateExpectedNodes(colour)] * len(self.x_values)
            plt.plot(self.x_values, listConvergence, color=colormap[colour], alpha=0.2)
        
        plt.ylabel('Number Of Nodes with Colour')
        plt.xlabel('Time Steps')
        plt.legend()
        plt.savefig("experimentGraph" + ".png")

        image = Image.open('experimentGraph.png')
        resized_image= image.resize((500,350), Image.ANTIALIAS)
        display = ImageTk.PhotoImage(resized_image)
        label = Label(self.output, image=display, text="Graph of Colours over time", justify=CENTER)
        label.image = display
        label.grid(row=4, column=0, columnspan=2, sticky = "NESW")

    def runExperiment(self):
        self.results = []

        #Calculates the expected steps until convergence, which is O(w^2 * n * log(n))
        totalWeight = self.getTotalWeight()
        expectedSteps = (totalWeight * totalWeight) * self.numOfAgents * math.log(self.numOfAgents, 10)
        print("Steps: " + str(expectedSteps))

        self.x_values = []
        self.y_values = {}

        #For each experiment
        self.simulation = Simulation(self.numOfAgents, self.numOfColours, self.weights, False)
        #Do the required number of steps
        self.doSteps(expectedSteps)
        colourResults = {}

        #For each colour see the representation in the graph and save to a dictionary
        for colour in range(self.numOfColours):
            colourRepresentation = self.calculateColourRepresentation(colour)
            colourResults[colour] = colourRepresentation

        #Save dictionary of colour results to the experiment
        self.results.append(colourResults)

        self.displayInputTable()
        self.displayWeightTable()
        self.createGraphNodesOverTime()


    def __init__(self, parent, agents, colours, weightsDict):
        #Call the simulation
        self.numOfAgents = agents
        self.numOfColours = colours
        self.weights = weightsDict

        #Initially we are on step 0
        self.stepNum = 0

        #Remove root window as this is the second window in the application
        # root = Tk()
        # self.root = root

        #Add this as a top level window with a title
        self.output = Toplevel(parent)
        self.output.title('Experimentation')

        self.runExperiment()

        oneStep = tk.Button(
                self.output,
                text="Rerun",
                command = lambda: self.runExperiment()
            )
    
        oneStep.grid(row = 5, column = 0, sticky = 'nesw', pady = 2, columnspan=2)

        




