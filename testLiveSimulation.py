import unittest
from liveSimulation import userOutput
import networkx as nx
import os
import tkinter as tk
from tkinter import ttk
from tkinter import *

class TestLiveSimulation(unittest.TestCase):

    #Create root window
    global test_window 
    test_window = tk.Tk()

    def test_simulation_creation(self):
        """
        Test that it creates an experiment correctly
        """
        #Create input
        test_agents = 5
        test_colours = 3
        test_weights_dict = {0: 1, 1: 1, 2: 2}
        test_create_drawing = False
        
        #Create graph with data
        testSimulation = userOutput(test_window, "connected", test_agents, test_colours, test_weights_dict)

        #Assert a simulation is created with all the required params
        self.assertEqual(test_agents, testSimulation.numOfAgents)
        self.assertEqual(test_colours, testSimulation.numOfColours)
        self.assertEqual(test_weights_dict, testSimulation.weights)

        self.assertEqual(0, testSimulation.stepNum)

    if __name__ == '__main__':
        unittest.main()