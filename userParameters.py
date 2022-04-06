import tkinter as tk
from tkinter import ttk
from tkinter import *
from turtle import left
from  main import Simulation
from liveSimulation import userOutput
from experiment import Experiment
import random
import math 

class UserParameters():

        def runSimulation(self):
                self.agents = self.numAgents.get()
                self.colours = self.numColours.get()
                self.weights = self.weightsInput.get()
                #print("agents: ", self.agents)

        def __init__(self):
            self.agents = 0
            self.colours = 0
            self.weights = ''
            self.weightsDict = {}
            
            self.window = tk.Tk()
            self.window.title('Simulation Parameters')

            fontBold = ("Helvetica", 14, "italic")
            self.fontRegular = ("Helvetica", 14)

            intro = tk.Label(padx = 10, text="Hello, welcome to the diversification protocol simulator. Please enter parameters and choose which option you would like to work with.", font=fontBold, wraplength=600, justify="left")
            intro.grid(row = 0, column = 0, sticky = W, pady = 2, columnspan = 2)

            #Create labels for welcome and introduction to window
            explanation = tk.Label(font= ("Helvetica", 14, "underline"), padx = 10, text="Enter parameters below:")
            explanation.grid(row = 1, column = 0, sticky = W, pady = 2, columnspan = 2)

            self.getAgents()
            self.getColours()
            self.getWeights()

            self.infoButtons()

            #Create a button for simulations
            #Create randomise weight button button
            buttonWeights = tk.Button(
                text="Random weights",
                command = self.populateWeights
            )
            buttonWeights.grid(row = 4, column = 2, sticky = W, pady = 2)

            #Create button for live simulation
            buttonSimulation = tk.Button(
                text="Run Interactive Simulation",
                command = self.on_press
            )
            buttonSimulation.grid(padx = 25, row = 6, column = 0, sticky = "NEWS", pady = 25)

            #Create button for experiments
            buttonExperiment = tk.Button(
                text="Run Experiments",
                command = self.experiment
            )
            buttonExperiment.grid(padx = 25, row = 6, column = 1, sticky = "NEWS", pady = 25)

            #Create information buttons
            buttonHelp = tk.Button(
                text="Help",
                command = self.simulationInfo
            )
            buttonHelp.grid(padx = 25, row = 6, column = 2, sticky = "NEWS", pady = 25)

            #Shows the window
            self.window.mainloop()

            

        def getAgents(self):
            #Create label and userinput, then pack into frame
            agentsLabel = tk.Label(font= self.fontRegular, text="Number of agents: ")
            self.numAgents = tk.Entry()

            agentsLabel.grid(padx = 25, row = 2, column = 0, sticky = W, pady = 2)
            self.numAgents.grid(row = 2, column = 1, sticky = "NEWS", pady = 2, columnspan=2)

        def getColours(self):
            #Create label and userinput, then pack into frame
            coloursLabel = tk.Label(font= self.fontRegular, text="Number of colours: ")
            self.numColours = tk.Entry()

            coloursLabel.grid(padx = 25, row = 3, column = 0, sticky = W, pady = 2)
            self.numColours.grid(row = 3, column = 1, sticky = "NEWS", pady = 2, columnspan=2)

        def getWeights(self):
            #Create label and userinput, then pack into frame
            weightsLabel = tk.Label(font= self.fontRegular, text="Weights of each colour as a list: ")
            self.weightsInput = tk.Entry()

            weightsLabel.grid(padx = 25, row = 4, column = 0, sticky = W, pady = 2)
            self.weightsInput.grid(row = 4, column = 1, sticky = "NEWS", pady = 2)

        def populateWeights(self):
            self.weightsInput.delete(0,END)
            numColours = self.numColours.get()
            try:
                tempWeights = []
                for i in range(int(numColours)):
                    randomWeight = random.randrange(1, 5)
                    tempWeights.append(randomWeight)
                #Remove last ','
                my_string = ','.join(map(str, tempWeights)) 
                self.weightsInput.insert(0, my_string)
            except:
                self.weightsErrorPopup()

        def simulationInfo(self):
            popup = tk.Toplevel(self.window)
            popup.wm_title("Simulation Help")

            textExplanation = """The simulation has two options.

The first option is an interactive simulation. This will allow you to monitor the behaviour of the simulation on a step-by-step basis so you can see how it progresses. 
This option is better for smaller amounts of agents (the recommendation is to have less than 40) so that it is easier to monitor the changes.
            
The second option is experimental. This will produce a graph of how many nodes have each colour versus time. 
This option works best for larger amounts of agents (the recommendation is 20+)
"""

            label = tk.Label(popup, wraplength=500, text=textExplanation, justify="left")
            label.grid(row=0, column=0, pady = 15, padx = 15)

            cancel = ttk.Button(popup, text="Go back", command=popup.destroy)
            cancel.grid(row=1, column=0, pady = 15, padx = 15)
            
        #When we press on the Start Simulation button
        def on_press(self):
            try:
                #Keep these as ints
                value_agents = int(self.numAgents.get())
                value_colours = int(self.numColours.get())
                self.agents = value_agents
                self.colours = value_colours

                #Weight input isn't in the format we want, so convert it
                self.weights = self.weightsInput.get()
                self.convertWeightsToDictionary(self.weights)

                #Make sure we have values for all
                if not value_agents or not value_colours or not self.weights:
                    print("Tip: you're missing a field")
                else:
                    #self.window.destroy()
                    #Call the simulation class
                    self.output = (self.agents, self.colours, self.weightsDict)
                    #self.sim = Simulation(self.output)
                    self.sim = userOutput(self.window, self.agents, self.colours, self.weightsDict)
            except:
                self.warningPopup()
                
        def warningPopup(self):
            popup = tk.Toplevel(self.window)
            popup.wm_title("Parameter Error")

            textExplanation = "Error: One of your paramters doesn't match the requested type or is missing. Please re-enter the parameter. \n If you want to find guidance on what each field expects, click on the information button next to each field."
            label = tk.Label(popup, wraplength=400, text=textExplanation, justify="left")
            label.grid(row=0, column=0)

            close = ttk.Button(popup, text="Ok", command=popup.destroy)
            close.grid(row=1, column=0, pady = 15, padx = 15)

        def weightsErrorPopup(self):
            popup = tk.Toplevel(self.window)
            popup.wm_title("Parameter Error")

            textExplanation = "Error: You don't have a parameter for number of colours. Please enter a parameter for colours and try again."
            label = tk.Label(popup, wraplength=400, text=textExplanation, justify="left")
            label.grid(row=0, column=0, pady = 15, padx = 15)

            close = ttk.Button(popup, text="Ok", command=popup.destroy)
            close.grid(row=1, column=0, pady = 15, padx = 15)

        def popup(self):
            popup = tk.Toplevel(self.window)
            popup.wm_title("Warning")

            label = tk.Label(popup, text="Woah there, your chosen parameters mean that the computation is going to take a while. Do you still want to continue?")
            label.grid(row=0, column=0)

            okay = ttk.Button(popup, text="Okay", command=lambda:[popup.destroy, self.runExperiment()])
            okay.grid(row=1, column=1, pady = 15, padx = 15)

            cancel = ttk.Button(popup, text="Go back", command=popup.destroy)
            cancel.grid(row=1, column=0, pady = 15, padx = 15)

        def getTotalWeight(self, weights):
            totalWeights = 0
            for weight in weights.values():
                totalWeights += weight
            return totalWeights

        def runExperiment(self):
            #self.window.destroy()
            #Call the simulation class
            self.experiment = Experiment(self.window, self.agents, self.colours, self.weightsDict)

        def experiment(self):
            try:
                #Keep these as ints
                self.agents = int(self.numAgents.get())
                self.colours = int(self.numColours.get())
                #Weight input isn't in the format we want, so convert it
                self.weights = self.weightsInput.get()
                self.convertWeightsToDictionary(self.weights)
                
                #If numbers to big, give warning
                totalWeight = self.getTotalWeight(self.weightsDict)
                total =  totalWeight * totalWeight * self.agents * math.log(self.agents, 10)
                if total > 20000:
                    self.popup()
                else:
                    self.runExperiment()
            except: 
                self.warningPopup()

        def convertWeightsToDictionary(self, weightsString):
            #The expected input of our weights is a string such as: '3,4,5' so we need to separate this for our Colours
            weightsList = weightsString.split(",")
            if len(weightsList) != self.colours:
                print("Make sure you have the same number of weights as the number of colours.")
            else:
                for colour in range(self.colours):
                    self.weightsDict[colour] = int(weightsList[colour])
            print(self.weightsDict)

        def infoButtons(self):
            #Create button for experiments
            infoAgents = tk.Button(
                text="Info",
                command = self.agentsInfo
            )
            infoAgents.grid(padx = 25, row = 2, column = 3, sticky = "NEWS")

            infoColours = tk.Button(
                text="Info",
                command = self.coloursInfo
            )
            infoColours.grid(padx = 25, row = 3, column = 3, sticky = "NEWS")

            infoWeights = tk.Button(
                text="Info",
                command = self.weightsInfo
            )
            infoWeights.grid(padx = 25, row = 4, column = 3, sticky = "NEWS")

        def agentsInfo(self):
            popup = tk.Toplevel(self.window)
            popup.wm_title("Agents Parameter")

            textExplanation = "The agents parameter takes a single integer as input. \n An example of the input expected is simply: 25"
            label = tk.Label(popup, wraplength=250, text=textExplanation, justify="left")
            label.grid(row=0, column=0, pady = 15, padx = 15)

            close = ttk.Button(popup, text="Ok", command=popup.destroy)
            close.grid(row=1, column=0, pady = 15, padx = 15)

        def coloursInfo(self):
            popup = tk.Toplevel(self.window)
            popup.wm_title("Colour Parameter")

            textExplanation = "The colour parameter takes a single integer as input. \n An example of the input expected is simply: 3"
            label = tk.Label(popup, wraplength=250, text=textExplanation, justify="left")
            label.grid(row=0, column=0, pady = 15, padx = 15)

            close = ttk.Button(popup, text="Ok", command=popup.destroy)
            close.grid(row=1, column=0, pady = 15, padx = 15)

        def weightsInfo(self):
            popup = tk.Toplevel(self.window)
            popup.wm_title("Weights Parameter")

            textExplanation = "The agents parameter takes a list of integers separeted with commas with no spaces as input, with the list being the same length as the number of colours. \n For 3 colours, an example input would be: 1,1,1"
            label = tk.Label(popup, wraplength=250, text=textExplanation, justify="left")
            label.grid(row=0, column=0, padx = 15)

            close = ttk.Button(popup, text="Ok", command=popup.destroy)
            close.grid(row=1, column=0, padx = 15)
    
#Call the window
UserParameters()