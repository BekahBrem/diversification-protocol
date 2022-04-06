#Imports
import networkx as nx
from agent import Agent
from graph import Graph
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from main import Simulation          

class userOutput():
    #simulation = ""

    #This function calls for the relevant number of steps to be performed
    def performSteps(self, numOfSteps):
        self.simulation.performSteps(numOfSteps)
        #Reload the updated image
        self.reloadImage()
        #Update step counter
        self.stepNum += numOfSteps
        self.updateStepCounter()
        #Update the table detailing colour distribution
        self.displayColourRepresentation()
        
    #Reloads the image in the window for every step
    def reloadImage(self):
        #Display Graph image
        image = Image.open('graph.png')
        display = ImageTk.PhotoImage(image)
        label = Label(self.simOutput, image=display, text="Graph at current timestep")
        label.image = display
        label.grid(row = 2, column = 0, sticky = W, pady = 2, columnspan = 3, rowspan=3)

    def updateStepCounter(self):
        self.textOutput = "Graph at step: " + str(self.stepNum)
        title = Label(self.simOutput, text=self.textOutput, font=('Helvetica', 18, 'bold'))
        title.grid(row = 0, column = 0, sticky = N, pady = 2, columnspan = 4)

    def getTotalWeight(self):
        totalWeights = 0
        for weight in self.weights.values():
            totalWeights += weight
        return totalWeights

    def getGoalWeight(self, colour):
        total = self.getTotalWeight()
        proportion = self.weights[colour]/total
        return round((proportion*100), 2)

    def calculateColourRepresentation(self, colour):
        total = self.getTotalWeight()
        colourCount = self.simulation.findNumberInGraph(int(colour))
        proportion = colourCount / self.numOfAgents
        return round((proportion*100), 2)

    def displayColourRepresentation(self):
        #Create table
        columns=('Colour', 'Current %', 'Goal %')
        tree = ttk.Treeview(self.simOutput, columns=columns, show='headings')
        for column in columns:
            tree.heading(column, text=column)    

        tree.grid(row=5, column=0, columnspan=4, sticky = "NESW" )

        temp = list(range(0, self.numOfColours))
        for colour in temp:
            tree.insert("", "end", values=(colour, self.calculateColourRepresentation(colour), self.getGoalWeight(colour)))

    #Called when object of this class is initialised
    def __init__(self, parent, agents, colours, weightsDict):
        #Call the simulation
        self.simulation = Simulation(agents, colours, weightsDict, True)
        self.numOfAgents = agents
        self.numOfColours = colours
        self.weights = weightsDict

        #Initially we are on step 0
        self.stepNum = 0


        #Add this as a top level window with a title
        self.simOutput = Toplevel(parent)
        self.simOutput.title('Simulation Output')

        #Add the step counter- this is initially step 0
        self.updateStepCounter()

        #Display Graph image
        self.reloadImage()

        self.displayColourRepresentation()

        #Buttons for simulation control
        #Button that performs 1 step
        oneStep = tk.Button(
                self.simOutput,
                text="1 Step",
                command = lambda: self.performSteps(1)
            )
        oneStep.grid(row = 2, column = 3, sticky = 'nesw', pady = 2)

        #Button that performs 25 steps
        twentyfiveSteps = tk.Button(
                self.simOutput,
                text="25 Steps",
                command = lambda: self.performSteps(25)
            )
        twentyfiveSteps.grid(row = 3, column = 3, sticky = 'nesw', pady = 2)

        #Button that performs 50 steps
        fiftySteps = tk.Button(
                self.simOutput,
                text="50 Steps",
                command = lambda: self.performSteps(50)
            )
        fiftySteps.grid(row = 4, column = 3, sticky = 'nesw', pady = 2)

        #Shows the window util it's manually closed
        self.simOutput.mainloop()









